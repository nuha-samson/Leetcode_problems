class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lst = [*range(0,max(nums)+1)]
        nums.sort()
        if lst == nums:
            return lst[-1]+1
        for i in range(len(lst)):
            if lst[i] not in nums:
                return lst[i]
