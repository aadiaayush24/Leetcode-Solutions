class Solution:
    def romanToInt(self, s: str) -> int:
        sym ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        val = 0
        for i in range(len(s)-1):
            if sym[s[i]] < sym[s[i+1]]:
                val -= sym[s[i]]
            else:
                val += sym[s[i]]
        val += sym[s[-1]]
        return val