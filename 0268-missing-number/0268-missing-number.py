class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums [0] == 1:
                return 0
            else:
                return 1
        else:
            for i in range(len(nums)-1):
                nums.sort()
                if nums[i]+1 != nums[i+1]:
                    return nums[i]+1
                elif nums[-1] == max(nums) and len(nums)-1 == nums[-1]:
                    return nums[-1]+1