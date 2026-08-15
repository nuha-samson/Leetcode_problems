from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Cs = Counter(s)
        Ct = Counter(t)
        if Cs == Ct:
            return True
        return False 
        