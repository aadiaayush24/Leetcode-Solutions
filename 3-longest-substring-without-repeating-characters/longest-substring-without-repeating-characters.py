class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        subStr = set()
        maxSize = 0
        for end in range(len(s)):
            currLet = s[end]
            if currLet in subStr:
                while s[start] != currLet:
                    subStr.remove(s[start])
                    start += 1
                start += 1
            else:
                subStr.add(currLet)
                if (len(subStr) > maxSize):
                    maxSize = len(subStr)
        return maxSize