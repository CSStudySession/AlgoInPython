'''
Meta version
Given current directory and change directory path, return final path.

For Example:
Curent                 Change            Output

/                    /facebook           /facebook
/facebook/anin       ../abc/def          /facebook/abc/def
/facebook/instagram   ../../../../.      /
'''

def change_path(cwd: str, cd: str) -> str:
    path = cwd + "/" + cd  # 先把两个path用'/'连起来
    stack = []
    for dir in path.split('/'):
        if dir == ".":
            continue
        elif dir == "..":
            if stack: 
                stack.pop()
        elif not dir:  # 注意 如果当前dir为空 题意需要回到根目录 
            stack.clear()
        else:
            stack.append(dir)

    return "/" + "/".join(stack)

# unit test
cwd1 = '/facebook/anin'
cd1 = '../abc/def'
print(change_path(cwd1, cd1))
cwd2 = '/'
cd2 = '/facebook'
print(change_path(cwd2, cd2))
cwd3 = '/facebook/anin'
cd3 = '..//def'
print(change_path(cwd3, cd3))

'''
用stack存最终返回path里面的子path
用'/'把input split成list
如果遇到“..”: 
如果有stack就pop. 如果“.” or "", continue. else stack.append
'''
def simplifyPath(self, path: str) -> str:
    if not path:
        return ""
    stack = []
    path_list = path.split("/")
    for item in path_list:
        if item == "." or item == "":
            continue
        elif item == "..": # 退到上一层
            if stack:
                stack.pop()
        else:
            stack.append(item)
    return "/" + "/".join(stack) # 前面加一个'/'