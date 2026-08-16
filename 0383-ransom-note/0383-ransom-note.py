from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        j = Counter(magazine)
        for i in r:
            if i in j:
                if r[i] > j[i]:
                    return False
            else:
                return False
        return True

