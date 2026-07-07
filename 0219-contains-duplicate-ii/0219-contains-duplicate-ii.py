class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pop = set()
        for i in range(len(nums)):
            if i > k:
                pop.remove(nums[i - k - 1])
            if nums[i] in pop:
                return True
            pop.add(nums[i])
        return False