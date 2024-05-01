class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        max_len = 0
        start = 0

        for i in range(len(s)):
            # Check for odd-length palindromes with s[i] as center
            len1 = self.expand_around_center(s, i, i)
            # Check for even-length palindromes with s[i] and s[i+1] as center
            len2 = self.expand_around_center(s, i, i + 1)

            # Update max_len and start index if a longer palindrome is found
            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
