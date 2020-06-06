""" Random Pick with Weight """
import random
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]
        
    def pickIndex(self) -> int:
		
		# this is where we pick the index
        N = random.uniform(0,1)
      
        flag = 1
        index = -1
        
        while flag:
            index +=1 
            if N <= self.w[index]:
                flag = 0
    
        return index
