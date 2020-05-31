'''Check If It Is a Straight Line'''
from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x_difference = coordinates[1][0] - coordinates[0][0]
        y_difference = coordinates[1][1] - coordinates[0][1]
        
        if x_difference == 0:
            slope = float("inf")
        else:
            slope = y_difference / x_difference
        
        lastCoordinate = coordinates[0]
        for i in range(2, len(coordinates)):
            coordinate = coordinates[i]
            x_difference = (coordinate[0] - lastCoordinate[0])
            y_difference = (coordinate[1] - lastCoordinate[1])
            
            if x_difference == 0:
                if slope != float("inf"):
                    return False
            elif (y_difference / x_difference) != slope:
                return False
        return True