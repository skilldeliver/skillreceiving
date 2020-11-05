# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        
        for i in c:
            if c[i] == 1:
                return s.index(i)
        return -1