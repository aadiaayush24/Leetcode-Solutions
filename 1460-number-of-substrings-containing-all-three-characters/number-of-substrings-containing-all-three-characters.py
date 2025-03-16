class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        idxLastSeen = [-1, -1, -1]
        count = 0
        for i in range(len(s)):
            currChar = s[i]
            idxLastSeen[ord(currChar)-ord('a')] = i
            minIndex = min(idxLastSeen)
            count += minIndex + 1 
        return count
            