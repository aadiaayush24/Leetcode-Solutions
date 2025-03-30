class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys) +1)
        dp[0] = 1
        for i in range(1, len(pressedKeys)+1):
            dp[i] = dp[i-1]
            key = pressedKeys[i-1]
            if (( i>= 4) and (key in ['7', '9']) and (pressedKeys[i-4:i] == key*4)):
                dp[i] += dp[i-4]
            if ( ( i>= 3) and pressedKeys[i-3: i] == key*3):
                dp[i] += dp[i-3]
            if ((i>=2) and pressedKeys[i-2:i] == key*2):
                dp[i] += dp[i-2]
            dp[i] = dp[i]%(10**9+7)

        return dp[-1]
             
            