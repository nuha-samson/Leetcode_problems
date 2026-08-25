from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)//2
        c = Counter(nums)
        for i,j in c.items():
            if j > m:
                return i
        return []
        