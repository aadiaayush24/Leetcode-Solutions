class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        w1 = list(word1)
        w2 = list(word2)
        while w1 or w2:
            if w1:
                res += w1.pop(0)
            if w2:
                res += w2.pop(0)
        return res
