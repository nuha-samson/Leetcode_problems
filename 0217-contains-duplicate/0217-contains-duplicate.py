class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashs = {}
        for i in range(len(nums)):
            if nums[i] not in hashs:
                hashs[nums[i]] = 1 + hashs.get(nums[i],0)
            elif nums[i] in hashs:
                return True
        return False
        