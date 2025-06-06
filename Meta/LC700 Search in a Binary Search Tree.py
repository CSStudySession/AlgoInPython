'''
在bst中找给定的val 找到就返回node
思路:按照bst的性质 根据val和当前node val的大小关系 往左或者又走即可
'''
# iterative T(h) worst N, S(1)
def searchBST(root, val: int):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root

# recursive T(h) worst N, S(h) worst N
def searchBST(root, val: int):
    if not root or val == root.val:
        return root
    return searchBST(root.left, val) if val < root.val \
        else searchBST(root.right, val)