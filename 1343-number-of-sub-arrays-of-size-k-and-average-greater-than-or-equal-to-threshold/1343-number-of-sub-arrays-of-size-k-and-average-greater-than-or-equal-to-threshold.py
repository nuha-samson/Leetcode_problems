class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0
        count = 0
        for i in range(k):
            window += arr[i]
        if window/k >= threshold:
            count += 1
        l = 0
        for i in range(k,len(arr)):
            window -= arr[l]
            window += arr[i]
            
            l += 1
            if window / k >= threshold:
                count += 1
        return count