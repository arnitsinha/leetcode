class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading whitespace
        s = s.lstrip()

        # Check if string is empty after removing whitespace
        if not s:
            return 0

        # Initialize variables
        sign = 1
        result = 0
        i = 0

        # Determine sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Apply sign
        result *= sign

        # Check if result is within the 32-bit signed integer range
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1

        return result
