class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        col = []
        v = []
        for i in range(len(nums)):
            if nums[i] == val:
                v.append(nums[i])
            else:
                col.append(nums[i])
        for j in range(len(col)):
            nums[j] = col[j]
                
        return len(col)