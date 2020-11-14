# Definition for singly-linked list.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        is_palindrome = False
        previous = tail = None

        while head != None:
            if is_palindrome:
                tail = tail.next
                is_palindrome = tail and head.val == tail.val
            if previous:
                if head.val == previous.val:
                    if head.next == previous.next or None not in (head.next, previous.next):
                        tail = previous
                        is_palindrome = True
                if previous.next and head.val == previous.next.val:
                     if head.next == previous.next.next or None not in (head.next, previous.next.next):
                        tail = previous.next
                        is_palindrome = True

            next_node = head.next
            head.next = previous
            previous = head
            head = next_node
        return is_palindrome and tail and tail.next == None

l = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1))))
s = Solution()
print(s.isPalindrome(l))