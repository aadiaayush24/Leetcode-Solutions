class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def findMinDistance(w1, w2, i, j, memo):
            if i >= len(w1):
                return len(w2) - j
            elif j >= len(w2):
                return len(w1) - i 
            if (i, j) in memo:
                return memo[(i, j)]
            if w1[i] == w2[j]:
                memo[(i, j)] = findMinDistance(w1, w2, i+1, j+1, memo)  # Characters match, move to next
            else:
                memo[(i, j)] = min(
                    findMinDistance(w1, w2, i+1, j+1, memo) + 1,  # Replace
                    findMinDistance(w1, w2, i, j+1, memo) + 1,    # Insert
                    findMinDistance(w1, w2, i+1, j, memo) + 1     # Delete
                )
            return memo[(i, j)]
        memo ={}
        return findMinDistance(word1, word2, 0, 0, memo)
