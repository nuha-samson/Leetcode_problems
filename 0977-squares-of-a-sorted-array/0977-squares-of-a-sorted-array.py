class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        j = 0
        k = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[j]) >= abs(nums[k]):
                res[i] = nums[j] ** 2
                j += 1
            else:
                res[i] = nums[k] ** 2
                k -= 1
        return res
