class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        start_index = 0
        curr_gas = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:  # Cannot start from current station
                start_index = i + 1
                curr_gas = 0

        if total_gas < total_cost:  # Total gas is not sufficient
            return -1
        else:
            return start_index if start_index < len(gas) else 0