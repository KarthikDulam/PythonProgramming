""" Permutation in String """

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        s1dict = {}
        # Create the dictionary for s1 string
        for char in s1:
            s1dict[char] = s1dict.get(char,0)+1
           
        # Our plan is to create a sliding window of s1 length in s2 and compare strings until we reach
        # end of s2
        i = 0
        while i < (lens2 - lens1)+1:
            
            slide = s2[i:lens1+i]
            if self.ispermutation(s1dict, slide) == True:
                return True
            i += 1
            
        return False
    
    def ispermutation(self, s1dict, slide):

        
        slidict = {}
           
        for char in slide:
            slidict[char] = slidict.get(char,0)+1
            
        if s1dict == slidict:
            return True
        
        return False