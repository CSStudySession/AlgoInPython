from typing import List

'''
有一个string list A, 里面每个string(tag)都不同.  另一个string list B是在A的基础上删掉了一些tags.
给定一个tag, 该tag一定在A里出现过, 要把它加入到list B中. 要求: tags之间的相对顺序不变.

例子:
list_A: {A B C D E F}
idx_A:   0 1 2 3 4 5 

list_B: {A  C  F}
idx_B:   0  1  2

给一个tag: D, 应该插入到list_B的下标2的位置.


思路: 二分
对B进行二分下标 第一次找到1-->对应字符C 然后去array_A里看 C的位置在2 D的位置在3 所以C小了 下次二分往右半边区间找
第二次找到2 -->对应字符F 再去array_A里看 F的位置在5 D的位置在3  5>3 找到了 --> 返回在F在array_B的下标2
需要对A建立一个索引: {str : index} 方便来一个tag时 能快速知道他在A的下标 
'''

def insert_with_order(tagsA: List[str], tagsB: List[str], tag: str) -> int:
    if not tagsA or not tagsB or len(tagsB) >= len(tagsA):
        return -1
    
    idx_dictA = {}
    for i in range(len(tagsA)):
        idx_dictA[tagsA[i]] = i
    
    left, right = 0, len(tagsB) - 1
    while left < right:
        mid = (left + right) // 2
        cur_tag = tagsB[mid]
        if idx_dictA[cur_tag] > idx_dictA[tag]:
            right = mid
        else:
            left = mid + 1
    return left

listA = ['A', 'B', 'C', 'D', 'E', 'F']
listB = ['A',  'C',  'F']

print(insert_with_order(listA, listB, 'D'))