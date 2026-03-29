# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        currentNode = head
        previosNode = None
        while currentNode.next is not None:
            next = currentNode.next
            currentNode.next = previosNode
            previosNode = currentNode

            currentNode = next

        currentNode.next = previosNode

        return currentNode

