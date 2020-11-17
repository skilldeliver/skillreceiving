# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min(len(s) for s in strs) if strs else 0
        prefix = str()

        for i in range(min_len):
            c = strs[0][i]
            common = True

            for s in strs[1:]:
                if c != s[i]:
                    common = False
                    break
            if common:
                prefix += c
            else:
                break
        return prefix
