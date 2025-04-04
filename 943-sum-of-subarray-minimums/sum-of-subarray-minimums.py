from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = (10 ** 9 + 7)
        stack = deque()
        n = len(arr)
        total = 0
        prev_smaller = [-1] * n
        
        for i in range(0, n):
            elem = arr[i]
            while (stack and arr[stack[-1]] >= elem):
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        next_smaller = [n] * n

        for i in range(n-1, -1, -1):
            elem = arr[i]
            while (stack and arr[stack[-1]] > elem):
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        # print(prev_smaller, next_smaller, sep="\n")
        for i in range(0, n):
            nse = next_smaller[i]
            pse = prev_smaller[i]

            possiblities = (nse - i) * (i - pse)
            total += (possiblities * arr[i])
            total = total % mod
        
        return total

            