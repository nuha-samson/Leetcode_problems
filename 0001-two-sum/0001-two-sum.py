from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashs:
                return [hashs[complement], i]
            hashs[nums[i]] = i
        return []