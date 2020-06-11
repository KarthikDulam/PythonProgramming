""" Search Insert Position """

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i , num in enumerate(nums):
            if target > num:
                count = i +1
            elif target == num:
                count = i
            elif i ==0 and target <num:
                count =0
        return count