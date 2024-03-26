class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        i, j = 0, len(s)-1
        if self.isPalindrome(s): return True
        while (i<j):
            if s[i] != s[j]:
                skipL, skipR = s[i+1: j+1], s[i: j]
                return self.isPalindrome(skipL) or self.isPalindrome(skipR)
            i+=1
            j-=1
        return True

    def isPalindrome(self, s):
        return s == s[::-1]
