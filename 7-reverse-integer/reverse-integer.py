class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Initialize result and flag for negative numbers
        result = 0
        negative = x < 0
        x = abs(x)

        # Reverse the digits of x
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        # Handle overflow/underflow
        if negative:
            result *= -1

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
