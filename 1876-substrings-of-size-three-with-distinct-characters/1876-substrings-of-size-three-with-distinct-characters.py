from collections import Counter
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        counter = Counter(s[:3])
        ans = 1 if len(counter) == 3 else 0
        l = 0
        for r in range(3, len(s)):
            counter[s[l]] -= 1
            if counter[s[l]] == 0:
                del counter[s[l]]
            l += 1
            counter[s[r]] += 1
            if len(counter) == 3:
                ans += 1
        return ans