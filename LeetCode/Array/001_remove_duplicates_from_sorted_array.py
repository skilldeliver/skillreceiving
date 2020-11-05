# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) not in [0, 1]:
            i = 0
            while i != len(nums) - 1:
                if nums[i] == nums[i+1]:
                    del nums[i]
                else:
                    i += 1
        return len(nums)
