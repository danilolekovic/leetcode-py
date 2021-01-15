class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        result = 0
        p = 'I'
        
        for char in s[::-1]:
            if numerals[char] < numerals[p]:
                result = result - numerals[char]
            else:
                result = result + numerals[char]
                p = char
                
        return result
