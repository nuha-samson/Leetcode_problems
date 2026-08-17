class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashs = {}
        for i in range(len(numbers)):
            ind = target - numbers[i]
            if ind in hashs:
                return [hashs[ind]+1,i+1]
            hashs[numbers[i]] = i
        return []