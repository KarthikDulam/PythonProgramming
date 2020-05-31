""" Counting Bits """
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        return (A := [0], any(A.append(A[i//2] + (i%2)) for i in range(1,num+1)))[0]