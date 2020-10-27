
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        indexes = list()

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    for k in indexes:
                        if k[0] <= i < k[1] and prices[j] - prices[i] > prices[k[1]] - prices[k[0]]:
                            print('once', k, i, j)
                            indexes.remove(k)
                            indexes.append((i, j))
                            break
                    else:
                        indexes.append((i, j))
        return indexes


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))