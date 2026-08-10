from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i
        