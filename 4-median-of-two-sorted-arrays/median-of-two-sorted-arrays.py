class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is smaller or equal to nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        
        # Binary search on nums1
        left, right = 0, m
        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = (total_len + 1) // 2 - partition_nums1
            
            # Calculate the elements around the partition
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            
            # Check if partition is correct
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # If total length is odd
                if total_len % 2 != 0:
                    return max(max_left_nums1, max_left_nums2)
                # If total length is even
                else:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2.0
            elif max_left_nums1 > min_right_nums2:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1