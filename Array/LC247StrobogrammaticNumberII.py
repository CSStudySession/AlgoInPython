class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        map = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        
        ret = []
        
        if n % 2 == 1:
            ret = ["0", "1", "8"]
            n -= 1
        else:
            ret = [""]
        
        while n:
            size = len(ret)
            while size:
                size -= 1
                cur = ret.pop(0)
                for key in map:
                    if n == 2 and key == "0":
                        continue
                    ret.append(key + cur + map[key])
            n -= 2
        return ret