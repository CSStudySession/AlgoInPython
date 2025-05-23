'''
given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
'''

'''
解法1:bfs. say N is the total number of nested elements in input: nested list + integers.
T: O(N)  S: O(N)
'''

def depthSum0(nestedList: List[NestedInteger]) -> int:
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
解法1:dfs. say N is the total number of nested elements in input: nested list + integers.
T: O(N)  S: O(N) for recursive call stack. e,g, [[[[1]]]]
'''
def depthSum1(nestedList: List[NestedInteger]) -> int:
    if not nestedList:
        return 0
    return self.dfs(nestedList, 1)

def dfs(nestedList: List[NestedInteger], level: int) -> int:
    ret = 0
    for item in nestedList: # 遍历的是List of NestedInteger
        if item.isInteger():
            ret += item.getInteger() * level
        else: # 不可以直接算的 用getList()取出来 递归往下传 level+1
            ret += self.dfs(item.getList(), level + 1)
    return ret