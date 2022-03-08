# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rvrs(node):
    if node.next is None:
        return node

    nextNode = node.next

    head = rvrs(nextNode)

    nextNode.next = node

    return head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        newHead = rvrs(head)
        head.next = None

        return newHead
