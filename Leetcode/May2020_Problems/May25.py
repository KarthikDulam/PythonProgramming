""" Uncrossed Lines """
from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], 1 + dp[i][j])
        return dp[-1][-1]        