""" Count Square Submatrices with All Ones """
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] > 0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res += matrix[i][j]
        return res