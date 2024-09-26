class Solution:
    def reverseWords(self, s: str) -> str:
        lastWasSpace = True
        wordStack = []
        currWord = ''
        for i in range(len(s)):
            if s[i] == ' ':
                if lastWasSpace:
                    continue
                else:
                    wordStack.append(currWord)
                    currWord = ''
                    lastWasSpace = True
            else:
                currWord += s[i]
                lastWasSpace = False
        if currWord:
            wordStack.append(currWord)

        res = ''
        while len(wordStack) > 1:
            res += wordStack.pop()+' '
        res += wordStack.pop()
        return res