# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        b=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                b=1
                break
        if b==0:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow