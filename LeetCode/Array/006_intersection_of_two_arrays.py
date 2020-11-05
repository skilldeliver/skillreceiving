# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ins = list()

        for n in nums1:
        	try:
        		nums2.remove(n)
        		ins.append(n)
        	except ValueError:
        		pass
        return ins