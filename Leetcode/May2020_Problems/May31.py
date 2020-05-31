''' Edit Distance'''
from collections import defaultdict
from itertools import chain
class Solution:
  def minDistance(self, s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    dp = defaultdict(int, chain(
      (((i, m), n - i) for i in range(n+1)), # base case for extra chars in s
      (((n, j), m - j) for j in range(m+1))  # base case for extra chars in t
    ))

    for i in range(n-1, -1, -1):
      for j in range(m-1, -1, -1):
        if s[i] == t[j]:
          dp[i,j] = dp[i+1,j+1] # match
        else:
          dp[i,j] = 1 + min(
            dp[i+1,j],  # delete
            dp[i,j+1],  # insert
            dp[i+1,j+1] # replace
          )

    return dp[0,0]