class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        setWordDict = set(wordDict)
        memo = {}
        def checkWordInDict(word: str):
            if word in memo:
                return memo[word]
            if not word:
                return True
            subStr = ""
            for i in range(0, len(word)):
                subStr += word[i]
                if subStr in setWordDict:
                    memo[subStr] = True
                    if (i+1 == len(word)):
                        return True
                    if (checkWordInDict(word[i+1:])):
                        return True
                else:
                    memo[word] = False

            return False
        return checkWordInDict(s)