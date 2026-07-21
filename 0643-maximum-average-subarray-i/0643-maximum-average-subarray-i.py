class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        curr_sum = 0
        l = 0
        for i in range(k):
            curr_sum += nums[i]
            max_sum = curr_sum
        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[l]
            max_sum = max(curr_sum,max_sum)
            l+=1
        return max_sum / k

        