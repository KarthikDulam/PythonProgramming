'''Valid Perfect Square'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        mid = num//2 
        
        if num == 1:
            return True
        elif num == 0:
            return False
        else:
            while (mid * mid > num):
                mid = int((mid + num / mid) / 2)
                
            return mid * mid == num
          
        return False
