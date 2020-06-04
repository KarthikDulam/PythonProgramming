'''Two City Scheduling '''
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        count1, count2, total = 0, 0, 0
        
        for cost1, cost2 in sorted(costs, key=lambda cost: -abs(cost[0] - cost[1])):
            if (cost1 < cost2 and count1 < N) or count2 == N:
                total += cost1
                count1 += 1
            else:
                total += cost2
                count2 += 1
        
        return total