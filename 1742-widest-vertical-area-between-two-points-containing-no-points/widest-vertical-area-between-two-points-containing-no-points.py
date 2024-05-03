class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort the points based on their x-coordinate
        points.sort(key=lambda x: x[0])
        
        max_width = 0
        # Iterate through the sorted points to find the maximum width
        for i in range(1, len(points)):
            max_width = max(max_width, points[i][0] - points[i-1][0])
        
        return max_width
