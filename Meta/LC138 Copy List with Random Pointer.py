from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''
思路1:dfs复制链表
dfs参数:当前要复制的原始节点,visited记录已经复制过的节点{原节点: 新节点}
dfs return: 复制后的节点
T(N) S(N)
'''     
def copy_random_list(head: "Optional[Node]") -> "Optional[Node]":
    # 使用一个字典保存原始节点到新节点的映射，避免重复拷贝
    visited = {}
    # 调用 dfs 辅助函数开始深拷贝
    return dfs(head, visited)

def dfs(node: "Node", visited: dict) -> "Node":
    # 如果当前节点为空，直接返回空
    if not node:
        return None
    # 如果当前节点已经被复制过，直接从哈希表中取出返回
    if node in visited:
        return visited[node]
    # 创建当前节点的新副本
    copy = Node(node.val)
    # 将原始节点与新节点建立映射关系，防止后续重复复制
    visited[node] = copy
    # 递归复制当前节点的 next 指针指向的节点
    copy.next = dfs(node.next, visited)
    # 递归复制当前节点的 random 指针指向的节点
    copy.random = dfs(node.random, visited)
    # 返回复制完成的节点
    return copy

'''
思路2:遍历3次 1.复制原节点和next 2.复制random 3.split copy list and orginal list
T(n) S(1) 
'''
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: 
        return None
    dummy = Node(0)
    dummy.next = head

    # copy node. copy placed at the next of original
    # dummy -> o1->c1->o2->c2-> ...
    while head:
        copy = Node(head.val)
        copy.next = head.next
        head.next = copy
        head = head.next.next

    # copy random
    head = dummy.next
    while head and head.next: # must have head.next
        if head.random: # some random is null
            head.next.random = head.random.next # head.random的next是h.random的copy 
        head = head.next.next # 已经插入 要走两步
    
    # split
    head = dummy.next.next
    res = dummy.next.next
    while head and head.next:
        tmp = head.next.next
        head.next = tmp
        head = head.next  # 已经去掉原来的head.next 只走一步
    return res

'''
variant: given a binary tree with random pointer. return a deep copy.
思路: dfs copy the original tree. 用visited dict记录原节点和复制节点
递归逻辑:
1. if not node, 返回 none 2. 如果node在visited中 之前复制过 返回复制节点.
3. 复制自己 记为copy.并存入visited. 递归复制左,右,random. 返回copy.
T(n) S(n)
'''
class TreeNode:
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None, random: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right
        self.random = random

def copy_with_random(head: Optional[TreeNode]) -> Optional[TreeNode]:
    visited = {}
    return dfs_copy(head, visited)

def dfs_copy(node:TreeNode, visited:dict) -> TreeNode:
    if not node:
        return None
    if node in visited:
        return visited[node]
    copy = TreeNode(node.val)
    visited[node] = copy
    copy.left = dfs_copy(node.left, visited)
    copy.right = dfs_copy(node.right, visited)
    copy.random = dfs_copy(node.random, visited)
    return copy