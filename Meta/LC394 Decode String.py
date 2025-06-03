'''用stack
- 初始化一个空栈 stack。
- 遍历字符串 s 中的每个字符：
如果当前字符不是 ]，直接压入栈中。
如果是 ]，说明遇到一个完整的编码结构，需要展开处理：
从栈中弹出字符，直到遇到 [，将中间字符拼接成 curr_str。
弹出 [。
继续从栈中弹出数字字符（考虑多位数），拼成字符串 curr_num。
计算 int(curr_num) * curr_str 将结果重新压入栈中 处理嵌套情况
遍历结束后，将栈中所有内容拼接起来就是最终解码结果。
T(n)  S(n)
'''
def decodeString(s: str) -> str:
    stack = []
    for char in s:
        ## Keep adding to Stack until a ']'
        if char != "]":
            stack.append(char)           
        else: 
            ## Extracting SubString to be Multiplied
            curr_str = ""
            while stack[-1] != "[":
                curr_str = stack.pop() + curr_str
            ## Pop to remove '['
            stack.pop()
            ## Extract full number (handles multi-digit, e.g. 10)
            curr_num = ""
            while stack and stack[-1].isdigit():
                curr_num = stack.pop() + curr_num
            ## Updating Stack with multiplied string
            curr_str = int(curr_num) * curr_str
            stack.append(curr_str)
    return "".join(stack)