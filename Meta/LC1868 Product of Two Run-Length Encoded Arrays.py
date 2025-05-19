'''
note:可能会先要求设计encode的数据结构 [1,1,1,2,2,2,2,2]-->[[1,3], [2,5]]
- 双指针对齐段
同时维护i指向encoded1的当前段 j指向encoded2的当前段
- 计算可用频次
对应段的剩余频次分别为cnt1=encoded1[i][1] cnt2=encoded2[j][1]
- 取最小频次做乘积
用min(cnt1, cnt2)作为本次可“配对”的长度curFreq 并计算对应值curValue=encoded1[i][0]*encoded2[j][0]
- 更新剩余频次与指针
如果 cnt1 < cnt2 说明 encoded1[i] 段用完，令 i++，并把 encoded2[j][1] -= cnt1
如果 cnt1 > cnt2 说明 encoded2[j] 段用完，令 j++，并把 encoded1[i][1] -= cnt2
如果相等 则同时 i++, j++
- 合并相邻同值段
每次得到新段[curValue, curFreq]时 若与结果数组res最后一个段的值相同 则只需把它的freq累加 否则追加一个新段
T(m+n) S(1)
'''
def findRLEArray(encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
    if not encoded1 or not encoded2:
        return []
    i, j = 0, 0
    res = []
    while i < len(encoded1) and j < len(encoded2):
        curValue = encoded1[i][0] * encoded2[j][0]
        cnt1 = encoded1[i][1]
        cnt2 = encoded2[j][1]
        
        if cnt1 < cnt2:
            i += 1
            curFreq = cnt1
            encoded2[j][1] = cnt2 - cnt1
        elif cnt1 > cnt2:
            j+= 1
            curFreq = cnt2
            encoded1[i][1] = cnt1 - cnt2
        else:
            i += 1
            j += 1
            curFreq = cnt1
        
        if res and res[-1][0] == curValue:
            res[-1][1] += curFreq
        else:
            res.append([curValue, curFreq])
    return res