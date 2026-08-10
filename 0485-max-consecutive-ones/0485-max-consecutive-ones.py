class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr= 0
        maxa = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                maxa = max(maxa,curr)
            else:
                curr = 0
        return maxa

        