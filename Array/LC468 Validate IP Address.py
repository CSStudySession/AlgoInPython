# Aaron solution
# Time O(N) 
# Space O(N)
def validIPAddress(self, queryIP: str) -> str:

    def is_ip_v4(s):   
        address = s.split(".")
        if len(address) != 4: return False 
        for item in address: 
            if not item.isdigit() or str(int(item)) != item or int(item) > 255: # str(int(item)) != item -> 判断是否有leading zeros. 如果有 int()会把前导0消除 在str()回去 就跟原始的item不同
                return False 
        return True 

    def is_ip_v6(s): 
        address = s.split(":")
        if len(address) != 8: return False 
        for item in address: 
            if len(item) < 1 or len(item) > 4: return False 
            for ch in item.lower(): # 先转换成小写
                if 'a' <= ch <= 'f' or '0' <= ch <= '9': 
                    continue 
                else: 
                    return False
        return True 

    if is_ip_v4(queryIP): return "IPv4" 
    return "IPv6" if is_ip_v6(queryIP) else "Neither"