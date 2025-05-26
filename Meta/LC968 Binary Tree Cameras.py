'''
思路:dfs+memo 对每个节点 定义三种状态 每种状态对应一个 以自己为根的树的最小cover代价
state0:no cameras cover me. invalid state,含义是希望我的parent nodes能cover我.
state1:I am covered, but I don't have camera.我被其他nodes覆盖了 我没有摄像头.
state2:I have camera.既能覆盖自己 也能覆盖周围节点.
dfs post orde traversal, 从叶子往上计算 每次返回(s0,s1,s2)给upper level caller.
最后根节点只能从s1,s2中选一个小的.
T(n) S(h)
'''
def minCameraCover(root):
    _, state1, state2 = dfs(root)
    return min(state1, state2)  # root必须被覆盖

def dfs(node):
    if not node:
        # 空节点默认是被覆盖但没有摄像头 给s2一个巨大的代价 意为不能装摄像头
        return (0, 0, float('inf'))

    l0, l1, l2 = dfs(node.left)
    r0, r1, r2 = dfs(node.right)

    # 状态0：该节点没被覆 左右必须是状态1(左右都被覆盖了且没装摄像头 如果装了当前节点就被覆盖了)
    state0 = l1 + r1

    # 状态1：该节点被覆盖但无摄像头 -> 左或右有摄像头
    state1 = min(l2 + min(r1, r2), r2 + min(l1, l2))

    # 状态2：该节点放了摄像头
    state2 = 1 + min(l0, l1, l2) + min(r0, r1, r2)

    return (state0, state1, state2)