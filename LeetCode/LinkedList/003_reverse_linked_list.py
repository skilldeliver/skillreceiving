# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
            if head is None:
                return None

            node = head
            last_node = ListNode(val=node.val, next=None)

            while node.next != None:
                node = node.next
                last_node = ListNode(val=node.val, next=last_node)
            return last_node

l = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
s = Solution()
n = s.reverseList(l)

while n.next != None:
    print(n.val, end=" -> ")
    n = n.next

print(n.val, end=" -> ")