'''
Given two lists with elements type which can be one of
- set
- word(string)

Check if the two lists matched?
For example
setEqual(["abc"], ["bac"]) --> False
setEqual(["abc"], ["abc"]) --> True
setEqual(["b", "a"], ["a", "b"]) --> True
setEqual([["a"], "b", "c"], ["a", "b", "c"]) --> False
setEqual(["a", "b", "c"], ["c", ["b", "a"]]) --> False
time complexity and space complexity

时间复杂度：
O(n)，其中 n 是列表中的元素总数（包括嵌套元素）。
每个元素只被处理一次，添加到集合的操作平均为 O(1)。

空间复杂度：
O(n)，在最坏情况下，每个元素都是唯一的或在不同的深度。
'''

from typing import List

def normalize(lst, count_set:set, depth:int):
    for item in lst:
        if isinstance(item, str):
            count_set.add((item, depth))
        else:
            normalize(item, count_set, depth + 1)

def count_occurrences(lst:List):
    count_set = set()
    normalize(lst, count_set, 0)
    return count_set

def setEqual(list1:List, list2:List):
    set1 = count_occurrences(list1) 
    set2 = count_occurrences(list2)
    # 比较两个列表中元素的出现情况
    return set1 == set2


# 测试
print(setEqual(["abc"], ["bac"]))  # False
print(setEqual([{"a", "b"}], [{"b", "a"}]))  # True
print(setEqual(["b", "a"], ["a", "b"]))  # True
print(setEqual([{"a"}, "b", "c"], ["a", "b", "c"]))  # False
print(setEqual(["a", "b", "c"], ["c", {"b", "a"}]))  # False
print(setEqual([""], [{""}]))  # False