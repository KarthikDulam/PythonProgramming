""" Contiguous Array """
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if(len(nums)<=1):
            return 0
      
        dict1={0:-1}
        count=0
        maximum=0
        for i,v in enumerate(nums):
          
            if(v==1):
                count+=1
            else:
                count-=1
           
            if count in dict1:
                maximum=max(maximum,i-dict1[count])
                
            else:
                dict1[count]=i
        return maximum 