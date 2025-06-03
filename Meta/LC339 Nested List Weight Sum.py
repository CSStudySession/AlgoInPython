import collections
'''
given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
'''
class NestedInteger:
    pass
'''
解法1:bfs. say N is the total number of nested elements in input: nested list + integers.
T: O(N)  S: O(N)
'''
def depthSum0(nestedList: list[NestedInteger]) -> int:
    if not nestedList:
        return 0
    level = 1
    queue = collections.deque(nestedList) #这里不要加"[]":把nestedList对象入队,不能变成list结构!
    ret = 0
    while queue:
        for _ in range(len(queue)): # 遍历当前层
            cur = queue.popleft()
            if cur.isInteger():
                ret += cur.getInteger() * level
            else:
                queue.extend(cur.getList()) # 取出当前item的内置items入队
        level += 1 # 当前层遍历完
    return ret

'''
解法2:dfs. say N is the total number of nested elements in input: nested list + integers.
T: O(N)  S: O(N) for recursive call stack. e,g, [[[[1]]]]
'''
def depthSum1(nestedList: list[NestedInteger]) -> int:
    if not nestedList:
        return 0
    return dfs(nestedList, 1)

def dfs(nestedList: list[NestedInteger], level: int) -> int:
    ret = 0
    for item in nestedList: # 遍历的是List of NestedInteger
        if item.isInteger():
            ret += item.getInteger() * level
        else: # 不可以直接算的 用getList()取出来 递归往下传 level+1
            ret += dfs(item.getList(), level + 1)
    return ret

'''
variant1: l = [1,[1,[3],1]] sum = 1*1 + 2*(1 + 3*3 + 1) = 23
思路:dfs. 每次dfs返回时 乘上对应的level 代表这层dfs代表的整体乘level
'''
def dfs_deep(nestedList, level) -> int:
    ret = 0
    for item in nestedList:
        if isinstance(item, int):
            ret += item
        else:
            ret += dfs_deep(item, level + 1)
    return ret * level # 注意是整体最后乘level

l = [1,[1,[3],1]] # 23
print(dfs_deep(l, 1))

'''
variant2: What if you had to define your own schema for NestedList and implement BFS / DFS?
注意, class Object适用于下面的bfs和dfs
bfs:使用queue按层遍历每一层对象。用 level 表示当前深度，逐层处理。
如果元素是整数，则乘以当前层数累加到结果中；
如果是嵌套对象 则展开其value加入队列 继续下一层
dfs:使用递归处理嵌套结构，参数 depth 表示当前深度；
如果是整数，乘以深度后返回
如果是嵌套对象 递归进入其value 深度加一
'''
class Object:
    def __init__(self):
        self.value: list['Object' | int]

def depth_sum_bfs(objs: list[Object]) -> int:
    queue = collections.deque(objs)
    level = 1
    sum = 0
    while queue:
        for _ in range(len(queue)):
            obj = queue.popleft()
            if isinstance(obj, int):
                sum += obj * level
            else:
                queue.extend(obj.value) # 把.value里的每个元素逐个加入队列 不是append()
        level += 1
    return sum

def depth_sum_dfs(objs: list[Object]) -> int:
    def dfs(objs, depth):
        sum = 0
        for obj in objs:
            if isinstance(obj, int):
                sum += obj * depth
            else:
                sum += dfs(obj.value, depth + 1)
        return sum
    return dfs(objs, 1)

'''
leetcode OG followup:实现接口
'''
class NestedInteger:
    def __init__(self, value=None):
        # value 可以是 int，NestedInteger 的列表，或者 None（空 list）
        if not value:
            self.value = []
        elif isinstance(value, int):
            self.value = value
        elif isinstance(value, list):
            self.value = value  # list of NestedInteger
        else:
            raise TypeError("Unsupported type")

    def isInteger(self) -> bool:
        return isinstance(self.value, int)

    def getInteger(self):
        return self.value if self.isInteger() else None

    def setInteger(self, value: int):
        self.value = value

    def add(self, elem: 'NestedInteger'):
        if self.isInteger():
            # 转换为 list 模式
            self.value = [elem]
        else:
            self.value.append(elem)

    def getList(self):
        return self.value if not self.isInteger() else None