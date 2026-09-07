# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        # prev, curr = None, head

        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # return prev

        previous, current = None, head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
        
        # # Recursive
        # if not head:
        #     return None

        # newHead = head # current node we are at in recursive call
        # if head.next: # if we can keep recursing
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead