""" Maximum Sum Circular Subarray """
from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_so_far, min_so_far, max_sum, min_sum, total_sum = A[0],A[0],A[0],A[0], sum(A)
        for i in range(1, len(A)):
            max_so_far = max(max_so_far+A[i],A[i])
            max_sum = max(max_sum,max_so_far)
            min_so_far = min(min_so_far+A[i],A[i])
            min_sum = min(min_sum,min_so_far)
        if min_sum==total_sum:
            return max_sum
        return max(total_sum-min_sum, max_sum)