class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            n, j = 0, len(i) - 1
            while n <= j:
                i[n], i[j] = 1 - i[j], 1 - i[n]
                n += 1
                j -= 1
        return image