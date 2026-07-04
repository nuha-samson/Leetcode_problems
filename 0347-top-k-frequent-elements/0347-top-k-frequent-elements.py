class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        f = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hash[i] = 1 + hash.get(i, 0)
        for i, j in hash.items():
            f[j].append(i)

        res = []
        for i in range(len(f) - 1, 0, -1):
            for j in f[i]:
                res.append(j)
                if len(res) == k:
                    return res