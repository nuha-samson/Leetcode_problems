class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 0
        r = len(skill) - 1
        skill.sort()
        count = 0
        add = 0
        while l < r:
            prod = skill[l] * skill[r]
            if add != 0 and skill[l] + skill[r] != add:
                return -1
                break
            add =  skill[l] + skill[r]
            l += 1
            r -= 1
            count += prod
        if len(skill) == 2 or count:
            return count