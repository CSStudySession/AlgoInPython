'''
OG. dummy指针+顺序遍历. 最后l1,l2最多剩下一个 直接cur.next接到剩下的那个即可.
T(n) S(1)
'''
'''

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    if list1:
        cur.next = list1
    else:
        cur.next = list2
    return dummy.next
'''
'''
variant1: given 3 sorted arrays, merge to one and return.
note that if 4 or more lists are given, use heap instead of pointers!
思路: three pointers. 每个指针指向三个array起点 谁小就选谁放入ret. 
注意while的条件是or + 如何处理out of bound的指针(给一个INF值).
T(n) S(1)
'''
def merge_three_sorted_array(nums_A:list[int], nums_B:list[int], nums_C:list[int]) -> list[int]:
    ret = []
    i, j, k = 0, 0, 0
    while i < len(nums_A) or j < len(nums_B) or k < len(nums_C):
        val_a = nums_A[i] if i < len(nums_A) else float('inf')
        val_b = nums_B[j] if j < len(nums_B) else float('inf')
        val_c = nums_C[k] if k < len(nums_C) else float('inf')
            
        cur_val = min(val_a, val_b, val_c)
        ret.append(cur_val)

        if cur_val == val_a:
            i += 1
        elif cur_val == val_b:
            j += 1
        else:
            k += 1
    return ret

# test
nums_A = [1,2,3,4]
nums_B = []
nums_C = [2,4,6,10]
# print(merge_three_sorted_array(nums_A, nums_B, nums_C))

'''
variant2: given 3 sorted arrays, merge to one and return WITHOUT duplicates!
思路:三指针 同variant1 在加入ret时 判断当前val是否与ret的最后一个数重复
T(n) S(1)
'''
def merge_three_sorted_array_no_dups(nums_A:list[int], nums_B:list[int], nums_C:list[int]) -> list[int]:
    ret = []
    i, j, k = 0, 0, 0
    while i < len(nums_A) or j < len(nums_B) or k < len(nums_C):
        val_a = nums_A[i] if i < len(nums_A) else float('inf')
        val_b = nums_B[j] if j < len(nums_B) else float('inf')
        val_c = nums_C[k] if k < len(nums_C) else float('inf')
            
        cur_val = min(val_a, val_b, val_c)
        if not ret or ret[-1] != cur_val: # no duplicates
            ret.append(cur_val)

        if cur_val == val_a:
            i += 1
        elif cur_val == val_b:
            j += 1
        else:
            k += 1
    return ret

nums_A = [1,2,3,4]
nums_B = []
nums_C = [2,4,6,10]
print(merge_three_sorted_array_no_dups(nums_A, nums_B, nums_C))