class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start: int, end: int):
        
            while start <= end:
                if s[start] != s[end]:  return False
                start += 1
                end -= 1
            return True
        
        def substringPartition(index, cand):
            if index == len(s):
                res.append(cand[:])
                return
            else:
                for i in range(index, len(s)):
                    if isPalindrome(index, i):
                        cand.append(s[index:i+1])
                        substringPartition(i+1, cand)
                        cand.pop()
                return
        
        cand = []
        res = []
        substringPartition(0, [])
        return res

                