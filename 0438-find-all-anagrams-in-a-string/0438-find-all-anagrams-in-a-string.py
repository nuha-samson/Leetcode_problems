from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
            
        p_count = Counter(p)
        window_count = Counter()
        result = []
        
        # Initialize the first window
        for i in range(len(p)):
            window_count[s[i]] += 1
        if window_count == p_count:
            result.append(0)
        
        left = 0
        for right in range(len(p), len(s)):
            window_count[s[right]] += 1 
            window_count[s[left]] -= 1 
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1
            if window_count == p_count:
                result.append(left)
        
        return result