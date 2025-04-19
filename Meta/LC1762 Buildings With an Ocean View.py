'''
ocean在右边.要求返回有o view元素的下标 下标从小到大返回.
'''

'''
solution: monotolic stack. stack存下标 下标对应元素的高度单调增 stack top的高度最小
T: O(n)  S: O(n)
'''
def findBuildings(heights: List[int]) -> List[int]:
    if not heights:
        return []
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop() # 栈顶对应的高度<=当前高度 则栈顶一定没有o view
        stack.append(i)
    return stack