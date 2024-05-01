class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Handle negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0

        # Reverse half of the integer
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # If the number of digits is odd, remove the middle digit from reversed_num
        return x == reversed_num or x == reversed_num // 10
