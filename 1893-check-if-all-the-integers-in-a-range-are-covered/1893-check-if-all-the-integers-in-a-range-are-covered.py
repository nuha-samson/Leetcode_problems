class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        w = []
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                w.append(j)
        if left in set(w) and right in set(w):
            return True
        return False
        


        
        
        