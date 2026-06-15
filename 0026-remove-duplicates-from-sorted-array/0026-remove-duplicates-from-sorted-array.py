class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] != nums[slow]:
                slow+=1
                nums[slow] = nums[i]
        return len(nums[:slow+1])