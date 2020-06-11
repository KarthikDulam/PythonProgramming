""" Is Subsequence """

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        seq = ''
        if s == '':
            return True
        elif t == '':
            return False
        else:
            
            for char in t:
                if c< len(s):
                    if char == s[c]:
                        seq += char
                        c+=1
        
        return s == seq
        