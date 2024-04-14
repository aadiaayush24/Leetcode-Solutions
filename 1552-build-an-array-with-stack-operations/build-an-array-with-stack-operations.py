class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        currTargetIndex = 0
        stack = []
        res = []
        start = 1
        while currTargetIndex != len(target) and start <= n:
            if target[currTargetIndex] == start:
                currTargetIndex += 1
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
            start += 1
        return res