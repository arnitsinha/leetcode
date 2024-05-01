class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    count = count + 1
        return count