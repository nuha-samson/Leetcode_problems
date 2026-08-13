from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        expected_gap = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            current_gap = arr[i + 1] - arr[i]
            if current_gap != expected_gap:
                return False
        return True
