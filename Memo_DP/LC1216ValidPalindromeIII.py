from typing import Dict, Tuple

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo: Dict[Tuple[int, int, int], bool] = {} 
        return self.dfs(0, len(s) - 1, s, k, memo)

    def dfs(self, i, j, s, count, memo) -> bool:
        if count < 0:      # all removal options used up
            return False
        if i >= j:         # i and j meet or corss
            return True
        if (i, j, count) in memo:  # (i, j, count) is a searched state
            return memo[(i, j, count)]
        
        ret = False
        if s[i] == s[j]:
            ret = self.dfs(i + 1, j - 1, s, count, memo)
        else:
            ret = self.dfs(i + 1, j, s, count - 1, memo) or self.dfs(i, j - 1, s, count - 1, memo)
        memo[(i, j, count)] = ret  # keep track of bool result of current state
        return ret