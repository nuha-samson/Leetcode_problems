from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashs = Counter(nums)
        for i in hashs:
            if hashs[i] >= 2:
                return True
        return False
        