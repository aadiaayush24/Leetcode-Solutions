class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        maxLen = 0
        for c in s:
            for i in range(len(sub)-1, -1, -1):
                if (sub[i] == c):
                    sub = sub[i+1:]
                    break
            sub += c
            print (sub)
            if len(sub) > maxLen:
                maxLen = len(sub)
        return maxLen