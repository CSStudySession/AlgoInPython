from collections import Counter
'''
思路:enumerate each digit and construct numbers.
计数预处理：
创建长度为10的数组 count count[i] 表示数字 i 在 digits 中出现的次数。
枚举所有合法三位偶数：
百位 i 只能是 1~9 首位不能是0 要有剩余次数
十位 j 0~9 同样要有剩余
个位 k 0~8 且是偶数 要有剩余
每次使用一个数字后递减其计数 枚举完成后再恢复（回溯）
最终返回所有构造出的数
T(n) from counter操作 最后的sorted()没有贡献 因为三位整数的偶数是常数个
S(1) counter和数组长度都固定
'''
def findEvenNumbers(digits: list[int]) -> list[int]:
    count = Counter(digits)
    ans = []
    # 枚举百位：1 ~ 9
    for i in range(1, 10):
        if count[i] == 0:
            continue
        count[i] -= 1  # 用掉一个i
        # 枚举十位：0 ~ 9
        for j in range(0, 10):
            if count[j] == 0:
                continue
            count[j] -= 1  # 用掉一个j
            # 枚举个位（必须是偶数）
            for k in range(0, 10, 2):
                if count[k] == 0:
                    continue
                # 构造一个三位偶数
                num = i * 100 + j * 10 + k
                ans.append(num)
            count[j] += 1  # 恢复j的使用
        count[i] += 1  # 恢复i的使用
    return sorted(ans)