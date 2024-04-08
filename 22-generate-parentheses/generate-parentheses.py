class Solution:
    '''void FIND_SOLUTIONS( parameters):
        if (valid solution):
            store the solution
            Return
        for (all choice):
            if (valid choice):
                APPLY (choice)
                FIND_SOLUTIONS (parameters)
                BACKTRACK (remove choice)
        Return'''
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s, o, c):
            if len(s) == 2*n:
                res.append(s)
                return          
            if o < n:
                generate(s +'(', o+1, c)
            if c < o:
                generate(s +')', o, c+1)
        res = []
        generate('', 0, 0)
        return res
        
                