class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = nums[0]

        for i in nums[1:]:
            n ^= i
        return n


s = Solution()
print(s.singleNumber([1,3,1,-1,3]))