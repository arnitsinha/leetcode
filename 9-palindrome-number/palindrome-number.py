class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert to string and compare with its reverse
        # return str(x) == str(x)[::-1]

        # Reverse the integer and compare with the original
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return reversed_num == original_x
