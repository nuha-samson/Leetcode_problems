class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        curr_sum = 0
        while l <= r:
            curr_sum = l**2 + r**2
            if curr_sum < c:
                l += 1
            elif curr_sum > c:
                r-=1
            elif curr_sum == c:
                return True
        return False

                         