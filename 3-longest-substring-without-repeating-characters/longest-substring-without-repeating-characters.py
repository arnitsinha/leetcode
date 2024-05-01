class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the index of the last occurrence of each character
        char_index = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If the character is already in the window, update the start index accordingly
            if char in char_index:
                start = max(start, char_index[char] + 1)
            # Update the index of the last occurrence of the character
            char_index[char] = end
            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)
        
        return max_length
