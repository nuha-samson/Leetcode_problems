class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # cook your dish here
        window = 0
        max_vowel = 0
        for i in range(k):
            if s[i] in "aeiou":
                window += 1
        max_vowel = window
        l = 0
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                window += 1
            if s[l] in "aeiou":
                window -= 1
            max_vowel = max(max_vowel,window)
            l+=1
        return (max_vowel)
    
    


        