class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        length, prev, index = 1, nums[0], 1
        
        for i in range(1, len(nums)):
            if nums[i] != prev:
                length += 1
                prev = nums[i]
                nums[index] = nums[i]
                index += 1
        
        return length
