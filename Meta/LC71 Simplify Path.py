'''
Meta version
Given current directory cwd already simlified, 
and change directory path cd, return final path.
For Example:
Curent                 Change            Output

/                    /facebook           /facebook
/facebook/anin       ../abc/def          /facebook/abc/def
/facebook/instagram   ../../../../.      /
/fb/a                empty               /fb/a
/a/c/d               /t/e/.././f            /t/f
思路:stack 用stack存cwd用/split之后的子结果 注意1.不存空 2.cd以/开头时 cwd先清空
再遍历cd用/ split的子结果 根据不用情况选择pop stack, continue, append stack.
最后返回/ + /.join(stack)
T(n) S(n)
'''
def change_directory(cwd: str, cd: str) -> str:
    if not cd:
        return cwd
    if cd[0] == '/':
        cwd = ''
    dirs = []
    for dir in cwd.split('/'):
        if dir: # 可能有'///a/'这种多个/相邻情况 多个/认为是一个 split后中间是空字符 忽略
            dirs.append(dir)
    
    for dir in cd.split('/'):
        if not dir:
            continue
        if dir == '.':
            continue
        elif dir == '..':
            if dirs:
                dirs.pop()
        else:
            dirs.append(dir)    
    return '/' + '/'.join(dirs)

# unit test
cwd1 = '/facebook/anin'
cd1 = '../abc/def'
print(change_directory(cwd1, cd1))
cwd2 = '/a/bb/c/d'
cd2 = '/facebook/./q/we'
print(change_directory(cwd2, cd2))
cwd3 = ''
cd3 = '/a/../c'
print(change_directory(cwd3, cd3))

'''
用stack存最终返回path里面的子path
用'/'把input split成list
如果遇到“..”: 
如果有stack就pop. 如果“.” or "", continue. else stack.append
'''
def simplifyPath(path: str) -> str:
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