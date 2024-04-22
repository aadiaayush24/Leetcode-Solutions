from collections import deque 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def allChildren(lock: str):
            res = []
            for i in range(4):
                add = lock[:i] + str((int(lock[i])+1)%10) + lock[i+1:]
                subtract = lock[:i] + str((int(lock[i])+9)%10) + lock[i+1:]
                res.extend([add, subtract])
            return res
        
        if '0000' in deadends:
            return -1
        
        queue = deque()
        queue.append(['0000', 0])
        turns = 0
        visited = set(deadends)
        while queue:
            curr, turns = queue.popleft()
            if curr == target:
                return turns
            for child in allChildren(curr):
                if child not in visited:
                    queue.append([child, turns+1])
                    visited.add(child)
        return -1


