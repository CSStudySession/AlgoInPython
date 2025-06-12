'''
为密室逃脱中心设计一个排行榜系统. 共有N个房间 M个参与者 
每位参与者从第一个房间开始 解谜后进入下一个房间 所有参与者互不干扰地独立解谜前进
要求
1: 统计当前在某个房间里的参与者人数。
2: 返回进度最靠前的k个参与者 若在同一房间则按进入该房间的先后顺序排序
3: 实现一个increment(participantId)函数 每当参与者完成一个房间 前进到下一个房间时被调用 需O(1)时间内
输入/输出接口
initialize(numPlayers: int, numRooms: int) -> None
increment(playerId: int) -> None  # O(1)
numPlayersInRoom(roomId: int) -> int
topPlayers(k: int) -> List[int]   # O(N + k) 或更优

clarifications:
- 时间复杂度要求?
increment(playerId) 必须是 O(1)
topPlayers(k) 最多O(N + K) 但可以通过增加空间优化性能
- What's beginning state? how do we break ties?
所有参与者最开始都在第一个房间(room 0) 顺序不重要 也不需要排名
从第一个房间之后 每个房间内部按进入顺序排序 即先进入的排前面
'''

'''
思路:核心是维护每个房间里参与者的顺序链表 使得:
- increment 可以 O(1) 将人从一个房间链表移除并加到下一个房间尾部
- topPlayers(k) 能够从最后一个房间向前扫描前 K 个参与者 按规则排序
数据结构设计
- 每个房间是一个双向链表(有 dummy head/tail)
- 每个参与者是一个链表节点 LinkedList
- 每个房间维护一个哈希表id_to_node 可O(1)找到参与者对应节点
- self.current_room[player_id] 表示该参与者当前在哪个房间
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Room:
    def __init__(self):
        self.head = Node(0)          # dummy head
        self.tail = Node(-1)         # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.id_to_node = {}         # participant_id -> LinkedList node
        self.player_cnt = 0

class Game:
    def __init__(self, n, m):  # n个room, m个参与人
        self.rooms = [Room() for _ in range(n)]
        self.n_participants = m
        self.current_room = {i: 0 for i in range(m)}   # 每个人起始在room0
        # 初始化所有人加入第0个房间
        first_room = self.rooms[0]
        self.rooms[0].player_cnt = m
        head = first_room.head
        for i in range(m):
            node = Node(i)
            head.next.prev = node
            node.next = head.next
            node.prev = head
            head.next = node
            head = node
            first_room.id_to_node[i] = node

    def increment(self, participant_id):  # T(1)
        cur_room_id = self.current_room[participant_id] # 取出room id
        if cur_room_id == len(self.rooms) - 1:
            return  # 已在最后一间房 不能再前进了

        cur_room = self.rooms[cur_room_id]     # 取出room对象
        node = cur_room.id_to_node[participant_id] # 取出人对应的node对象

        # 从当前房间链表中移除该节点
        node.prev.next = node.next
        node.next.prev = node.prev
        del cur_room.id_to_node[participant_id]
        cur_room.player_cnt -= 1

        # 加入到下一个房间尾部
        nxt_room = self.rooms[cur_room_id + 1]
        tail = nxt_room.tail
        node.prev = tail.prev
        node.next = tail
        tail.prev.next = node
        tail.prev = node
        nxt_room.id_to_node[participant_id] = node
        self.current_room[participant_id] += 1
        nxt_room.player_cnt += 1

    def numPlayersInRoom(self, room_id: int) -> int:  # T(1)
        return self.rooms[room_id].player_cnt

    def topPlayers(self, k: int) -> list[int]: # T(n+k)
        result = []
        # 从最后一个房间往前找
        for room_id in range(len(self.rooms) - 1, -1, -1):
            node = self.rooms[room_id].head.next
            while node != self.rooms[room_id].tail and len(result) < k:
                result.append(node.val)
                node = node.next
            if len(result) >= k:
                break
        return result
    
'''
followup: 如何优化topPlayers()? 
维护一个全局排序结构, 比如一个SortedList 里面装一个自定义对象playerStatus 排序规则按照:
当前房间号(大的优先)
同房间内的进入顺序(早的优先) 可以用一个timestamp表示进入房间的时间或者编号 
这样可以在 increment() 时维护好排序, topPlayers(k)直接取前k项
查找时:T(k) 更新时:T(logm)
'''