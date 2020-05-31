'''Single Element in a Sorted Array'''
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = n-1

        while l<r:
            m    = l + (r-l)//2
            curr = nums[m]
            prev = nums[m-1]
            nex  = nums[m+1]
            
            if curr==prev: 
                if (r-(m-1)+1)%2==0:  # Check if right-subarray has even number of elements (counting from both instances of curr)
                    r = m - 2  # If yes, skip both instances of curr and look in the left-subarray
                else:
                    l = m + 1 # If no, skip both instances of curr and look in the right-subarray
                    
            elif curr==nex:
                if (r-(m)+1)%2==0: # Check if right-subarray has even number of elements (counting from both instances of curr)
                    r = m - 1  # If yes, skip both instances of curr and look in the left-subarray
                else:
                    l = m + 2 # If no, skip both instances of curr and look in the right-subarray
            else:
                return curr

        return nums[l]    # Only one element left, has to be the non-repeated one