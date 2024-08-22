'''
注意这里是set 下面有另一个版本 是list的
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

时间复杂度：
O(n)，其中 n 是列表中的元素总数（包括嵌套元素）。
每个元素只被处理一次，添加到集合的操作平均为 O(1)。

空间复杂度：
O(n)，在最坏情况下，每个元素都是唯一的或在不同的深度。
'''
from typing import List, Union

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
'''
print(setEqual(["abc"], ["bac"]))  # False
print(setEqual([{"a", "b"}], [{"b", "a"}]))  # True
print(setEqual(["b", "a"], ["a", "b"]))  # True
print(setEqual([{"a"}, "b", "c"], ["a", "b", "c"]))  # False
print(setEqual(["a", "b", "c"], ["c", {"b", "a"}]))  # False
print(setEqual([""], [{""}]))  # False
'''

'''

Given two lists with elements type which can be one of
- list
- word(string)

Check if the two lists matched?
For example
setEqual(["abc"], ["bac"]) --> False
setEqual(["abc"], ["abc"]) --> True
setEqual(["b", "a"], ["a", "b"]) --> True
setEqual([["a"], "b", "c"], ["a", "b", "c"]) --> False
setEqual(["a", "b", "c"], ["c", ["b", "a"]]) --> False

思路: 用(元素, 层数, 在该层出现的次数)三元组 标识每个元素
把三元组 存在dict中 key是(元素，层数) val是在该层出现的次数
dfs构建该dict 最后比较两个list分别生成的dict是否元素和对应的值均相同

时间复杂度：
O(n)，其中 n 是列表中的元素总数（包括嵌套元素）。
每个元素只被处理一次，添加到集合的操作平均为 O(1)。

空间复杂度：
O(n)，在最坏情况下，每个元素都是唯一的或在不同的深度。
'''
from collections import defaultdict

def normalize(item: Union[str, List], depth: int, count_dict: dict[tuple[str, int], int]):
    if isinstance(item, str):
        count_dict[(item, depth)] += 1
    elif isinstance(item, list):
        for sub_item in item:
            normalize(sub_item, depth + 1, count_dict)

def count_occurrences(lst: List) -> dict[tuple[str, int], int]:
    count_dict = defaultdict(int)
    normalize(lst, 0, count_dict)
    return count_dict

def listEqual(list1: List, list2: List) -> bool:
    count_dict1 = count_occurrences(list1)
    count_dict2 = count_occurrences(list2)
    return count_dict1 == count_dict2

# 测试
print(listEqual(["abc"], ["bac"]))  # False
print(listEqual(["abc"], ["abc"]))  # True
print(listEqual(["b", "a"], ["a", "b"]))  # True
print(listEqual([["a"], "b", "c"], ["a", "b", "c"]))  # False
print(listEqual(["a", "b", "c"], ["c", ["b", "a"]]))  # False
print(listEqual(["a", "a", ["b", "b"], "c"], ["a", ["b", "b"], "a", "c"]))  # True
print(listEqual(["a", ["a", "b", "a"], "b"], ["a", ["b", "a", "a"], "b"]))  # True