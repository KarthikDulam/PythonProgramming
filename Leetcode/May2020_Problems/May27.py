""" Possible Bipartition """
from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        distSet = defaultdict(set)
        for i, j in dislikes:
            distSet[i].add(j)

        A, B = set(), set()
        while distSet:
            if A:
                toRemove = []
                for i, js in distSet.items():
                    if i in A or js.intersection(B):
                        A.add(i)
                        B.update(js)
                    elif i in B or js.intersection(A):
                        B.add(i)
                        A.update(js)
                    else:
                        continue
                    toRemove.append(i)
                if A.intersection(B):
                    return False
                if toRemove:
                    for i in toRemove:
                        distSet.pop(i)
                else:
                    A, B = set(), set()
            else:
                i = list(distSet.keys())[0]
                A.add(i)
                B.update(distSet[i])
                distSet.pop(i)
        return True