class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def findMinDistance(w1, w2, i, j):
            if (i == len(w1)):
                return len(w2) - j
            elif (j == len(w2)):
                return len(w1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            if (w1[i] == w2[j]):
                memo[(i, j)] = findMinDistance(w1, w2, i+1, j+1)
            else:
                memo[(i, j)] = min(findMinDistance(w1, w2, i+1, j)+1, findMinDistance(w1, w2, i, j+1)+1)
            return memo[(i, j)]
        return findMinDistance(word1, word2, 0, 0)