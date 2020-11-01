class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        try:
        	while True:
        		nums.remove(0)
        		count += 1
        except ValueError:
        	nums += ([0] * count)