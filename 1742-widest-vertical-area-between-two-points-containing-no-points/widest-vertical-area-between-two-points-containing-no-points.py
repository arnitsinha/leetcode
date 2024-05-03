class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Extract x-coordinates from the points
        x_coords = sorted(x[0] for x in points)
        
        max_width = 0
        # Iterate through the sorted x-coordinates to find the maximum width
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i-1])
        
        return max_width
