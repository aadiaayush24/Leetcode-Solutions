class Solution:
    def checkValidString(self, s: str) -> bool:
        def checkParanthesis(string, index, count):
            if count < 0:
                return False 
            if index == len(string):
                return count == 0
            
            if (index, count) in dp:
                return dp[(index, count)]
            
            c = s[index]

            if c == '(':
                dp[(index, count)] = checkParanthesis(string, index+1, count+1)
            elif c == ')':
                if count == 0:
                    dp[(index, count)] = False
                else:
                    dp[(index, count)] = checkParanthesis(string, index+1, count-1) 
            else:
                dp[(index, count)] = (checkParanthesis(string, index+1, count+1) or
                                checkParanthesis(string, index+1, count-1) or
                                checkParanthesis(string, index+1, count))
            return dp[(index, count)]
        
        dp = {}
        return checkParanthesis(s, 0, 0) 
        