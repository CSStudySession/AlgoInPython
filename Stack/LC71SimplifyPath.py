
class Solution:
    # 先split成list. 用stack
    # 如果遇到“..”: 
    #      如果有stack就pop. 如果“.” or "", continue. else stack.append
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathList = path.split("/")
        
        for string in pathList:
            if string == "." or string == "":
                continue
            elif string == "..":
                if stack:
                    stack.pop() # ..意思是退到上一层 
            else:
                stack.append(string)
                
        return "/" + "/".join(stack)