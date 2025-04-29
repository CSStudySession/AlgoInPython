from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
用stack辅助构建树结构
1. 读取数字，创建一个新的节点。
2. 遇到左括号 '('，就开始处理左子树。
3. 左子树处理完成后 再遇到下一个 '(' 开始处理右子树。
4. 括号结束表示当前子树结束，需要回到父节点继续构建。
每次遇到新子节点，都将父节点压入栈，处理完毕后再弹出返回上一层。
'''
def str2tree(s: str) -> Optional[TreeNode]:
    if not s:
        return None
    root = TreeNode()
    stack = [root]
    idx = 0
    while idx < len(s):
        node = stack.pop()
        if s[idx].isdigit() or s[idx] == '-': # 截取数字
            val, idx = get_num(s, idx)
            node.val = val
            if idx < len(s) and s[idx] == '(': # 数字之后的'(' 是左子树
                if idx + 1 < len(s) and s[idx + 1] == ')': # 跳过空的左节点
                    idx += 1
                    continue
                stack.append(node) # 当前节点压栈 处理完左子节点再回来
                node.left = TreeNode()
                stack.append(node.left)

        elif node.left and s[idx] == '(': # 左孩子存在了 要处理右孩子
            stack.append(node)
            node.right = TreeNode()
            stack.append(node.right)
        idx += 1 # 注意要更新idx
    if stack:
        return stack.pop()
    return root

def get_num(s, idx) -> tuple:
    is_neg = False
    if s[idx] == '-':
        is_neg = True
        idx += 1
    
    num = 0
    while idx < len(s) and s[idx].isdigit():
        num = num * 10 + int(s[idx])
        idx += 1
    if is_neg: # 根据符号返回正负数
        return (-num, idx)
    return (num, idx)