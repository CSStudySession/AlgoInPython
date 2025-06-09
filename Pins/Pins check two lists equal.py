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

Clarification:
Order does not matter
同一个集合中不允许重复元素 但嵌套结构中可以重复. 合法:['1', ['2', '1']] 不合法"['1','1',['2']] 
嵌套没有限制（任意层级的嵌套集合是合法的）
空集合 [] 是合法输入
'''

'''
解法1:序列化为字符串+排序
将集合序列化成有序字符串 便于比较
n:# of total elements(str+collections)->T(nlogn) 
S(h + t), h for stack, t for serialized strings
每层有排序操作 n个elements 每个最多被处理一次
'''
from typing import Union
SetItem = Union[str, list['SetItem']]  # 递归定义类型

def serialize(item: SetItem) -> str:
    if isinstance(item, str):
        return item
    serialized_children = [serialize(child) for child in item]
    serialized_children.sort()
    return "{" + "".join(serialized_children) + "}"

def sets_equal(a: SetItem, b: SetItem) -> bool:
    return serialize(a) == serialize(b)

'''
解法2:自定义Comparator + sort后比较
直接对集合对象排序并逐项比较 避免字符串拼接开销
n:# of total elements(str+collections)->T(nlogn) 
每层有排序操作 n个elements 每个最多被处理一次
S(h + t), h for stack, t for tmp strings as sorting key.
'''
def custmizted_sort(item: SetItem) -> SetItem:
    if isinstance(item, str):
        return item
    # 先对每个子元素递归 custmizted_sort
    children = [custmizted_sort(child) for child in item]
    # 排序，先排字符串，再排集合，集合内也已排好
    children.sort(key=lambda x: (0, x) if isinstance(x, str) else (1, serialize(x)))
    return children

def sets_equal_structural(a: SetItem, b: SetItem) -> bool:
    return custmizted_sort(a) == custmizted_sort(b)

'''
解法3:每个字符串和子集合映射为唯一整数ID, 通过比较ID是否相等判断集合相等性.
避免频繁排序与字符串操作 适合大数据量场景
n:# of total elements(str+collections)->T(nlogn) 
每层有排序操作 n个elements 每个最多被处理一次
T(n) 两个哈希表存字符串和集合结构 没有冗余字符串创建
'''
from typing import Dict, Tuple

word_id_map: Dict[str, int] = {}
set_id_map: Dict[Tuple[int], int] = {}
id_counter = [0]  # 使用列表作为可变对象模拟引用

def get_id(item: SetItem) -> int:
    if isinstance(item, str):
        if item not in word_id_map:
            word_id_map[item] = id_counter[0]
            id_counter[0] += 1
        return word_id_map[item]
    
    child_ids = tuple(sorted(get_id(child) for child in item))
    if child_ids not in set_id_map:
        set_id_map[child_ids] = id_counter[0]
        id_counter[0] += 1
    return set_id_map[child_ids]

def sets_equal_id(a: SetItem, b: SetItem) -> bool:
    # 清空全局状态以确保复用安全
    word_id_map.clear()
    set_id_map.clear()
    id_counter[0] = 0
    # python执行时 从左到右 先算a再算b 两者共用一套maps
    return get_id(a) == get_id(b)


# test
A = ["a", ["b", "c"]]
B = [["c", "b"], "a"]
print(sets_equal_id(A, B))