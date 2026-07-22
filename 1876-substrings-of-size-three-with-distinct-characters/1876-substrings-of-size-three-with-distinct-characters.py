from collections import Counter
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = Counter(s[:3])
        a = 1 if len(count) == 3 else 0
        l = 0 
        for i in range(3,len(s)):
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l += 1
            count[s[i]] += 1
            if len(count) == 3:
                a += 1
        return a