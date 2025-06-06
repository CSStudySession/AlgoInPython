'''
Implement a function to convert a string such as 5(4(2)(3))(60(7)) to a binary tree.
      5
     / \
    4   6
   / \    \
  2   3    7

思路:
递归解析 + 括号匹配. 将字符串递归地拆解成三部分:根节点、左子树、右子树
1. 提取根节点值：
我字符串开头扫描连续的数字字符，构造出当前子树的根节点。
2. 识别左子树
如果后面紧跟一个括号 '(' 用一个 left_cnt 变量做括号计数：
每遇到一个 '(' 加一，')' 减一；
当 left_cnt 回到 0 说明找到了当前左子树的完整表达式边界
提取这段字符串作为左子树部分。
3. 识别右子树
右子树字符串就在左子树之后的一段，用类似方式处理。
递归构建：
对左右子树字符串递归调用相同逻辑 最终构建出整颗树
T(n ^ 2) in worst caase, tree is a "linked list format", each time we need to 
scan the remaining string to get ')' index: N + N - 1 + N - 2 + ... + 1 -> T(n^2)
S(h), h is tree height, worst case S(n) 

'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def parse_str(s):
    i = 0
    while i < len(s) and s[i].isdigit():
        i += 1
    val = int(s[:i])  # 提取根节点的值

    j, open_cnt = i + 1, 1
    while j < len(s): # j最终停在左子树右括号的位置
        if s[j] == '(':
            open_cnt += 1
        elif s[j] == ')':
            open_cnt -= 1
        if open_cnt == 0:
            break
        j += 1 

    left = s[i + 1: j]  # 提取左子树字符串 i,j分别指向左右括号位置
    right = s[j + 2: -1] if j + 2 < len(s) else ""  # 提取右子树字符串
    return val, left, right

def construct_tree(s):
    if len(s) == 0:
        return None
    val, left, right = parse_str(s)
    root = Node(val)
    root.left = construct_tree(left)
    root.right = construct_tree(right)
    return root

s = '5(4(2)(3))(6(7))'
print(construct_tree(s).right.val)










