""" Course Schedule """
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = {key: 0 for key in range(numCourses)}
        graph = defaultdict(list)

        for j,i in prerequisites:
            graph[i].append(j)
            degree[j] += 1

        lst_no_dep = [ x for x in range(numCourses) if degree[x] == 0]

        # Topological sort
        stk = []
        while lst_no_dep:
            cs = lst_no_dep.pop()
            stk.append(cs)
            for cs_greater in graph[cs]:
                degree[cs_greater] -= 1
                if degree[cs_greater] == 0:
                    lst_no_dep.append(cs_greater)
        return len(stk) == numCourses        