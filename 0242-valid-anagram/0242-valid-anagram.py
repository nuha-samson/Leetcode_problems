class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = Counter(s)
        hasht = Counter(t)
        ok = True
        if len(t) == len(s):
            for i in hasht:
                if hashs[i] != hasht[i]:
                    ok = False
                    break
            return True if ok else False
        else:
            return False