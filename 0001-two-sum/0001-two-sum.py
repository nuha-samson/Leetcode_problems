from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashs:
                return [hashs[diff],i]
            hashs[nums[i]] = i
        return []