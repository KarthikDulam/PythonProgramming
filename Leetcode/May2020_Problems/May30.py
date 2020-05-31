""" K Closest Points to Origin """
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distdict = {}
        i= 0
        outlist = []
        for val in points:
            distdict[i]= distdict.get(i,0)+math.sqrt((val[0]**2)+(val[1]**2))
            i+= 1
        sorteddict = sorted(distdict.items(), key=lambda x: x[1])
        #print(sorteddict)
        for i, val in zip(range(K),sorteddict):
            outlist.append(points[val[0]])
            
        return outlist