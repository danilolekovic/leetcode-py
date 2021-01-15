class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # this is just fibonnaci sequence
        
        table = { 0:1, 1:1 }
        
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        
        return table[n]
