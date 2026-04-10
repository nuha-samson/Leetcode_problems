class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i] == k:
                    count += 1
        return count