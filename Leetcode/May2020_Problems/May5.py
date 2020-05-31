''' First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chardict = {}
        
        if s == '':
            return -1
        
        for char in s:
            chardict[char]=chardict.get(char,0)+1
        
        #chardict_sorted = sorted(chardict)
        
        for char in chardict.keys():
            if chardict[char] == 1:
                return s.find(char)
                
            
        return -1