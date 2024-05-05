class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key = lambda x: x[1] - x[0], reverse= True)
        i = 0
        initialEnergy = tasks[0][1]
        currEnergy = initialEnergy
        sumEnergy = 0
        while (i != len(tasks)):
            if currEnergy >= tasks[i][1]:
                currEnergy -= tasks[i][0]
                sumEnergy += tasks[i][0]
                i += 1
            else:
                initialEnergy += (tasks[i][1] - currEnergy)
                currEnergy = initialEnergy - sumEnergy
        return initialEnergy
        