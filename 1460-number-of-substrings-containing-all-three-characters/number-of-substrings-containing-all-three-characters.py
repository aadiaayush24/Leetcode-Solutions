class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        idxLastSeen = {'a':-1, 'b':-1, 'c':-1}
        l = len(s)
        count = 0
        for i in range(l):
            currChar = s[i]
            idxLastSeen[currChar] = i
            minIndex = min(idxLastSeen.values())
            count += minIndex + 1 
        return count
            