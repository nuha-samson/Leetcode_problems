from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()        
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        if window_count == s1_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            window_count[s2[right]] += 1
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            
            left += 1
            
            if window_count == s1_count:
                return True
        
        return False