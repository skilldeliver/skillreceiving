# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

class Solution:
    @staticmethod
    def constrain32bit(x: int) -> int:
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0

    def reverse(self, x: int) -> int:
        if x < 0:
            num = int(f'-{str(abs(x))[::-1]}')
            return Solution.constrain32bit(num)
        num = int(str(x)[::-1])
        return Solution.constrain32bit(num)