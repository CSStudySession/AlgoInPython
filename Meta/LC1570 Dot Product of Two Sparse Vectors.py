from typing import List
class SparseVector:
    # method 1: build a set to store the index of non-zero element
    # check if new vec.nums[i]!=0 and in self.set, calculate total.
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.set = set()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.set.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if not vec: return 0
        total = 0
        for i in range(len(vec.nums)):
            if i in self.set and vec.nums[i] != 0:
                total += self.nums[i] * vec.nums[i]
        return total

    # method 2: create self.pairs = <index, value> for non-zeros. 
    # two pointers to iterate through the two vectors to calculate the dot product.
    def __init__(self, nums: List[int]):
       self.pairs = [] #build (index, value) pair
       for i in range(len(nums)):
        if nums[i] != 0:
            self.pairs.append((i, nums[i]))
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if not vec: return 0
        total = 0
        p, q = 0, 0
        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]: # index相等才相乘
                total += self.pairs[p][1] * vec.pairs[q][1]
                p += 1 # 注意都要往后移动
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]: # 因为构建pairs时是顺序的 所以谁idx小谁往后移动
                p += 1
            else:
                q += 1
        return total

    # followup: what if the lengths of both vectors differ drastically?
    '''
    思路: binary search. 在长的vector上做binary search.
    举例: [(idx, non-zero val)]
    vec_a = [[1, 3], [6, 9]]
    vec_b = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 7]]
    for each vec_a: binary search on vec_b to find matching index
    T(len_shorter_vec * log(len_longer_vec))
    '''
    def dotProduct_binary_search(self, vec: 'SparseVector') -> int:
        if not vec: return 0
        shorter, longer = ( # 分配长短 注意语法
            (self.pairs, vec.pairs)
            if len(self.pairs) < len(vec.pairs)
            else (vec.pairs, self.pairs)
        )
        ret = 0
        for pair in shorter:
            idx = self.binary_search_idx(longer, pair[0])
            if idx == -1: # 找不到match的index
                continue
            ret += pair[1] * longer[idx][1] # 找到match index, 就相乘
        return ret
    
    def binary_search_idx(self, longer: List[tuple[int]], target: int) -> int:
        left, right = 0, len(longer) - 1
        while left < right:
            mid = (left + right) // 2
            if longer[mid][0] == target:
                return mid
            elif longer[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        return left if longer[left][0] == target else -1
