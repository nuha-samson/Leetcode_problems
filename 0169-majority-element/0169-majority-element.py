class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            elif nums[i] in count:
                count[nums[i]] += 1
        for i,j in count.items():
            if j > len(nums) // 2:
                return i

        