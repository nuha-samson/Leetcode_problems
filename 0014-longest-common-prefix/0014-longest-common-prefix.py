class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if not strs:
            return ''
        else:
            letter = []
            left = 0
            right = 0
            while left < len(strs[0]) and right < len(strs[-1]):
                if strs[0][left] == strs[-1][right]:
                    letter.append(strs[0][left])
                else:
                    break
                left += 1
                right += 1
            return "".join(letter)