# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoListsLOL(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if (l1 is l2 is None):
            return None

        head = None

        while (l1.next != None or l2.next != None):
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next

            if head is None:
                head = node
            else:
                n = head
                while n.next != None:
                    n = n.next
                n.next = node
        return head

l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

s = Solution()
l3 = s.mergeTwoLists(l1, l2)
print(l3.val, end=" -> ")

while l3.next != None:
    l3 = l3.next
    print(l3.val, end=" -> ")