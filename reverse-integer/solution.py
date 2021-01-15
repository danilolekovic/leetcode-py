class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        revInt = sign * int(str(abs(x))[::-1])
        return revInt if -(2**31) - 1 < revInt < 2**31 else 0
