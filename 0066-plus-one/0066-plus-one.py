class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = "".join(map(str, digits))
        num = int(nums) + 1
        return list(map(int, str(num)))
