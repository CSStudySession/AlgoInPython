'''
乘法时候需要计算cur * prev_operand, 先把前一个prev_operand(递归传下来的)减掉 再加回 e.g.:
1 2 3 4 5 --> 1 + 2 + 3 + 4 * 5
              ^ ^ ^ ^ ^ ^ ^ == 10 but here we want 4*5 so:
        we do 1 + 2 + 3 + 4 + (- 4) + (4 * 5)
T(4^N) 每次dfs 有四种选择, idx最大能取到N, N is len(num)
S(N) recursion stack could take O(N), auxiliary tmp could take O(N)
TODO: 生成两个简单用例
'''

def addOperators(num: str, target: int) -> list[str]:
    ret = []
    dfs(num, target, "", 0, 0, 0, ret)
    return ret

def dfs(num, target, tmp, idx, prev_oprd, total, ret):
    if idx == len(num) and total == target:
        ret.append(tmp)
        return
    for j in range(idx, len(num)):
        cur = int(num[idx: j + 1])
        if len(num[idx: j + 1]) > 1 and num[idx] == '0': # 判断leading 0.
            break # idx为起点的所有dfs都可以不用试了 idx起点是leading 0
        if idx == 0: # 首次dfs 直接把当前值pass下去 不用考虑符号
            dfs(num, target, str(cur), j + 1, cur, cur, ret)
        else:
            dfs(num, target, tmp + '+' + str(cur), j + 1, cur, total + cur, ret)
            dfs(num, target, tmp + '-' + str(cur), j + 1, -cur, total - cur, ret)
            # 乘法分支 pass给下面的操作数为:当前切出来的数(cur) * 之前传下来的数(prev_oprd)
            dfs(num, target, tmp + '*' + str(cur), j + 1, cur * prev_oprd, total - prev_oprd + prev_oprd * cur, ret)