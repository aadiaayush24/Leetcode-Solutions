class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def longestSubstringRecursive(start, end):
            if end < k:
                return 0
            dictMap = dict()
            for cInd in range(start, end):
                currChar = s[cInd] 
                if currChar in dictMap:
                    dictMap[currChar] += 1
                else:
                    dictMap[currChar] = 1
            
            for mid in range(start, end):
                currChar = s[mid]
                if dictMap[currChar] >= k:
                    continue
                midNext = mid + 1
                while (midNext < end and dictMap[s[midNext]] < k):
                    midNext += 1
                return max(longestSubstringRecursive(start, mid), longestSubstringRecursive(midNext, end))
            return end - start
        return longestSubstringRecursive(0, len(s))