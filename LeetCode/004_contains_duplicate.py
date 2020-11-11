from collections import defaultdict


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_occur = defaultdict(int)

        for n in nums:
        	nums_occur[n] += 1

        	if nums_occur[n] > 1:
        		return True

        return False
