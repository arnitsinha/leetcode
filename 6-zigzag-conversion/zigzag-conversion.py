class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        # Create rows to store characters
        rows = [''] * numRows

        # Initialize the direction and row index
        direction = -1  # Up or Down
        row = 0

        for char in s:
            # Append the character to the current row
            rows[row] += char
            # Change direction if at the top or bottom row
            if row == 0 or row == numRows - 1:
                direction *= -1
            # Move to the next row based on the direction
            row += direction

        # Concatenate all rows to get the zigzag pattern
        return ''.join(rows)
