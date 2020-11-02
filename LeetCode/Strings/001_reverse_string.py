# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        t = list()
        for _ in range(len(s)):
            t.append(s.pop())
        s += t
