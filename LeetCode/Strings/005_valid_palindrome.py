# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

from string import ascii_letters, digits

class Solution:
	def isPalindrome(self, s: str) -> bool:
		alphanumeric_chars = ascii_letters + digits

		filtered_s = str()

		for c in s:
			if c in alphanumeric_chars:
				filtered_s += c 
		return filtered_s.lower() == filtered_s[::-1].lower()
