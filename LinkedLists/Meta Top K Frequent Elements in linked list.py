'''
Given an linked list nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''
from collections import defaultdict
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def topKFrequent(head: ListNode, k: int) -> list:
    # Step 1: Count the frequency of each element in the linked list
    frequency = defaultdict(int)
    current = head
    
    while current:
        frequency[current.val] += 1
        current = current.next
    
    # Step 2: Use a min-heap to keep track of the top k elements
    min_heap = []
    
    for num, freq in frequency.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Step 3: Extract the elements from the heap
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    
    return result

# Helper function to create linked list from list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test case 1
nums = create_linked_list([1, 1, 1, 2, 2, 3])
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]

# Test case 2
nums = create_linked_list([1])
k = 1
print(topKFrequent(nums, k))  # Output: [1]