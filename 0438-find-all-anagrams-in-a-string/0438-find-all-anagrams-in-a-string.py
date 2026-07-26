from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        window = [0] * 26
        l = 0
        p_count = [0] * 26
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        for r in range(len(s)):
            window[ord(s[r]) - ord('a')] += 1
            while r - l + 1 > len(p):
                window[ord(s[l]) - ord('a')] -= 1
                l += 1 
            if window == p_count:
                ans.append(l)
        return ans