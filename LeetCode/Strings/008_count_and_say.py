# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        said = Solution.countAndSay(self, n - 1)
        new_said, count = str(), int()
        char = said[0]

        for c in said:
            if c == char:
                count += 1
            else:
                new_said += f"{count}{char}"
                char = c
                count = 1
        new_said += f"{count}{char}"
        return new_said

s = Solution()
print(s.countAndSay(4))
