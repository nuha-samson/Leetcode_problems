class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == max(nums):
            arr = set(range(len(nums)+1))-set(nums)
            return arr.pop()           
        return max(nums) + 1