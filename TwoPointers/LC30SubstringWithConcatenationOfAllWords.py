
from typing import List
from typing import Dict
import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret: List[int] = []
        len_s = len(s)
        len_ws = len(words)
        len_w = len(words[0])
        
        ws_dict: Dict[str, int] = collections.defaultdict(int)
        for word in words:
            ws_dict[word] += 1

        for i in range(len_w): # interate each group
            wd_dict: Dict[str, int] = collections.defaultdict(int)
            cnt = 0
            for j in range(i, len_s - len_w + 1, len_w):
                if j >= i + len_w * len_ws:
                    fst_wd = s[j - len_ws * len_w: j - len_ws * len_w + len_w]
                    wd_dict[fst_wd] -= 1
                    if wd_dict[fst_wd] < ws_dict[fst_wd]:
                        cnt -= 1
                wd = s[j: j + len_w]
                wd_dict[wd] += 1
                if wd_dict[wd] <= ws_dict[wd]:
                    cnt += 1
                if cnt == len_ws:
                    ret.append(j - len_w * (len_ws - 1))
        return ret