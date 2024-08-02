class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursion(index):
            if index == n:
                return True
            if index in memo:
                return memo[index]
            for i in range(index+1, n+1):
                if s[index:i] in wordDict and recursion(i):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        memo = {}
        wordDict = set(wordDict)
        n = len(s)
        return recursion(0)