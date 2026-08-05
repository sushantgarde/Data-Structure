import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = list(zip(*matrix[::-1]))
        
        for i in range(len(matrix)):
            matrix[i] = list(rotated[i])