class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index != index2 and num + num2 == target:
                    indices.append(index)
                    indices.append(index2)
                    return indices
        
        return indices
        