# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current: 
            # save current.next so we don't lose it
            next_node = current.next 
            # point current towards the previous value to reverse
            current.next = previous 
            # set previous to the current node before we start next cycle
            previous = current
            # current moves to next node
            current = next_node
        return previous # previous will stop at last node, current will stop at None
        # return the new head, now that list is reversed