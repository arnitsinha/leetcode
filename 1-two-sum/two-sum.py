class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}
        # Populate the dictionary with indices of elements
        for i, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = []
            num_indices[num].append(i)
        
        # Iterate through the array to find the pair
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                # If the complement exists and it's not the same as num
                if complement != num:
                    return [i, num_indices[complement][0]]
                # If the complement is the same as num, check if there are more than one occurrences
                elif len(num_indices[complement]) > 1:
                    return [i, num_indices[complement][1]]
