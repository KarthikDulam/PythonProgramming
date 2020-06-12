""" Sort Colors """
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        two_pointer = len(nums)-1
        curr_pos = 0
        
        while curr_pos<=two_pointer:
            if nums[curr_pos]== 0:
                nums[curr_pos],nums[zero_pointer]= nums[zero_pointer],nums[curr_pos]
                zero_pointer +=1
                curr_pos += 1
            elif nums[curr_pos]==2:
                nums[curr_pos],nums[two_pointer]= nums[two_pointer], nums[curr_pos]
                two_pointer-=1
                
            else:    
                curr_pos += 1
            