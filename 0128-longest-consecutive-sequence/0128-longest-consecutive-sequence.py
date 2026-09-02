class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        for x in nums:
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                max_len = max(max_len,y-x)
        return max_len
        