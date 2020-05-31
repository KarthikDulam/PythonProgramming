'''Find the Town Judge'''
from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        valdict = {}
        everyone = set()
        
        if N == 1:
            return 1
        
        for val in trust:
            valdict[val[1]] = valdict.get(val[1],0)+1
            everyone.add(val[0])
        
        for val in valdict.keys():
            if val not in everyone and valdict[val] == N-1:
                return val
            
        return -1
