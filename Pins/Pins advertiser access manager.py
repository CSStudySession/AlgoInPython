'''
用户被分组 比如 "World" > "Europe" > "France" > "Paris"。
Advertisers可以对某一组用户(Group)授予访问权限 用于广告投放
如果广告主获得了对某一组的访问权限 他们同时拥有所有子组的访问权限 撤销访问时也是递归地对子组生效
要求实现3个接口
grant_access(advertiser_id, group_id)
revoke_access(advertiser_id, group_id)
check_access(advertiser_id, group_id) -> bool
注意:
授权是递归传递的 授权父组等于授权所有子组。撤销也是递归的。要高效支持check操作
需要支持动态建树(group与sub-group的建立)和动态的权限更新

思路:
整个 group 结构为一棵树，每个节点为一个 PinnerGroupNode。
每个 group 节点维护一个字典：
accessStatus: Dict[advertiser_id] = accessRecord(status, timestamp)
每次授权或撤销操作只更新当前 group 的 accessStatus。
每次访问检查 check_access 时，从当前 group 向上查找，找到最近的一次授权或撤销操作（取时间戳最大的那一个）。
避免每次授权或撤销都去更新整棵子树，提高效率。
clarification question:假设# of groups >> avg # of layer of group access? (n >> h) 
时间复杂度在code的函数上已标注. T(k*n) k:# of advertiser, n:# of groups -> 每个广告主都可以对每个group有访问状态.
'''
import time
# 单个广告主的访问记录：状态 + 时间戳
class accessRecord:
    def __init__(self, status:bool=None, timestamp:float=None):
        self.status = status
        self.timestamp = timestamp

    def update_status(self, status):
        self.status = status
        self.timestamp = time.time()

# 每个 group 节点的数据结构
class GroupNode:
    def __init__(self, ID, parent=None):
        self.ID = ID                  # 当前 group ID
        self.parent = parent          # 父节点引用
        self.accessStatus = {}        # 广告主 ID -> accessRecord
        self.children = set()         # 子节点 ID 集合

# 主实现类
class AccessManager:
    def __init__(self, root_ID):
        self.nodes_map = {}  # group ID -> PinnerGroupNode
        self.nodes_map[root_ID] = GroupNode(root_ID, None)

    # 添加子 group（建立 parent-child 关系）  T(1)
    def add_child(self, parent_ID, child_ID):
        self.nodes_map[child_ID] = GroupNode(child_ID, parent_ID)
        self.nodes_map[parent_ID].children.add(child_ID)

    # 授权访问某个 group  T(1)
    def grant_access(self, adv_ID, node_ID):
        if adv_ID not in self.nodes_map[node_ID].accessStatus:
            self.nodes_map[node_ID].accessStatus[adv_ID] = accessRecord()
        self.nodes_map[node_ID].accessStatus[adv_ID].update_status(True)

    # 撤销访问某个 group. T(1)
    def revoke_access(self, adv_ID, node_ID):
        if adv_ID not in self.nodes_map[node_ID].accessStatus:
            self.nodes_map[node_ID].accessStatus[adv_ID] = accessRecord()
        self.nodes_map[node_ID].accessStatus[adv_ID].update_status(False)

    # 检查是否拥有访问权限 T(h), h is height of this group.
    # 从目标节点开始 一路向上check到group root,找timestamp最近的一次status update作为答案
    def check_access(self, adv_ID, node_ID):
        prev_ts, prev_st = None, None # 最近一次的timestampe, status. 初始化None意为未知

        # 自底向上递归检查访问状态
        return self.dfs_check(node_ID, adv_ID, prev_ts, prev_st)

    # 带时间戳优先级的递归权限检查
    def dfs_check(self, node_ID, adv_ID, prev_ts, prev_st):
        if not node_ID:
            return prev_st if prev_st else False

        node = self.nodes_map[node_ID]

        if adv_ID in node.accessStatus:
            record = node.accessStatus[adv_ID]
            # 如果比已有记录时间更新 则更新状态
            if prev_ts is None or record.timestamp > prev_ts:
                prev_ts = record.timestamp
                prev_st = record.status
        # 向父节点递归
        return self.dfs_check(node.parent, adv_ID, prev_ts, prev_st)
    
# test
s = AccessManager("World")
s.add_child("World", "Europe")
s.add_child("Europe", "France")
s.add_child("France", "Paris")
s.grant_access("ad_1", "France")

print(s.check_access("ad_1", "Paris"))   # True
s.revoke_access("ad_1", "World")
print(s.check_access("ad_1", "Paris"))   # False