""" Interval List Intersections """
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        
        for x in range(len(A)):
            for y in range(len(B)):
                
                if B[y][1] >= A[x][0] and B[y][0] <= A[x][1]:
                    result.append([max(A[x][0],B[y][0]),min(A[x][1],B[y][1])])
        return result