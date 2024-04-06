class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        extraClose = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    extraClose.append(i)
        stack.extend(extraClose)
        stack.sort()
        newS = ''
        for i in range(len(s)):
            if not stack or i != stack[0]:
                newS += s[i]
            elif stack:
                stack.pop(0)
        return newS

        