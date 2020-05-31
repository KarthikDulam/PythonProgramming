""" Find All Anagrams in a String """
from collections import Counter
from operator import delitem

class Solution:
  def findAnagrams(self, T, S):
    A, B, res = Counter(S), Counter(T[:len(S)]), []
    if A == B: res.append(0)
    for i in range(len(S), len(T)):
      B.update(T[i])
      c = T[i-len(S)]
      B.subtract(c) if B[c] > 1 else delitem(B, c)
      if A == B: res.append(i-len(S)+1)
    return res