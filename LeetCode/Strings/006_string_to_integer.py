# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        r = r'^\s*((?:-|\+)?\d+).*$' 
        m = re.search(r, s)

        try:
            n = int(m.group(1))

            if n >= 2**31 - 1:
                return 2**31 - 1
                
            if n <= -2**31:
                return -2**31
            return n

        except Exception:
            return 0

s = Solution()
print(s.myAtoi("  -0012a42"))