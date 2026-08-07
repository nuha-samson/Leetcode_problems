from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i]  in my_dict:
                return my_dict[target - nums[i]],i
            my_dict[nums[i]] = i


        