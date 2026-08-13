class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = ''
        for i in s[::-1].strip():
            if i == ' ':
                break
            else:
                st += i
        return len(st)
