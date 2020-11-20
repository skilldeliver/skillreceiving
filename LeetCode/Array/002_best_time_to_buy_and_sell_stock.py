
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        max_total = -2**31

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                total = 0
                if prices[j] > prices[i]:
                    total += prices[j] - prices[i]
                total += Solution.maxProfit(self, prices[j+1:])

                if total > max_total:
                    max_total = total
        return max_total

s = Solution()
print(s.maxProfit( [7,1,5,3,6,4]))
