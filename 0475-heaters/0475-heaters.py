from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = len(houses) - 1
        min_radius = 0
        heater_idx = 0
        while left <= right:
            i = houses[left]  
            while heater_idx < len(heaters) - 1 and abs(heaters[heater_idx + 1] - i) <= abs(heaters[heater_idx] - i):
                heater_idx += 1
            min_dist = abs(heaters[heater_idx] - i)
            min_radius = max(min_radius, min_dist)
            left += 1
        return min_radius
