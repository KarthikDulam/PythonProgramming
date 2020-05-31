""" Sort Characters By Frequency """

class Solution:
    def frequencySort(self, s: str) -> str:
        strdict = {}
        string = ''
        for char in s:
            strdict[char] = strdict.get(char,0)+1
            
        strdict_sort = sorted(strdict.items(), key=lambda x: x[1], reverse=True)
        
        for i in strdict_sort:
            string = string + (str(i[0]) * i[1])
            
        return string