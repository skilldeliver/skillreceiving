# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        last_n = [node]

        while node.next != None:
            node = node.next

            if len(last_n) < n:
                last_n.append(node)
            else:
                pre_last = last_n.pop(0)
                last_n.append(node)

        last_node = last_n.pop(0)

        if last_node == head and n == 1:
            return None

        if last_node.next:
            last_node.val = last_node.next.val
            last_node.next = last_node.next.next
        else:
            pre_last.next = None 

        return head

s = Solution()
l = ListNode(1)
n = s.removeNthFromEnd(l, 1)
print(n.val, end=" -> ")

while n.next != None:
    n = n.next
    print(n.val, end=" -> ")
