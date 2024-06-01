class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        res = 0
        for c in s[1:]:
            curr = ord(c)
            res += abs(curr-prev)
            prev = curr
        return res