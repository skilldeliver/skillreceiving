# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) != 0:
        	part = len(nums) - (k % len(nums))
        	nums += nums[:part]
        	del nums[:part]