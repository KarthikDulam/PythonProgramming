""" Reverse String """
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        char = ''
        lst_index = len(s)-1
        for val in range(len(s)//2):
            
            char= s[val]
            s[val]= s[lst_index-val]
            s[lst_index-val]=char