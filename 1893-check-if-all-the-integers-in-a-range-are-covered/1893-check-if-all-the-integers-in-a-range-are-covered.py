class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        w = []
        
        for i in range(len(ranges)):
            for j in range(ranges[i][0], ranges[i][1] + 1):
                w.append(j)
        
        covered = set(w)
        
        # Check EVERY number from left to right
        for i in range(left, right + 1):
            if i not in covered:
                return False
        
        return True