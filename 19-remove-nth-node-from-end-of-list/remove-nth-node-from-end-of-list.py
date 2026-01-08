# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next7
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            curr=curr.next
            count=count+1
        curr=head
        if n==count:
            head = head.next
        for i in range(count):
            if count-i==n+1:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
        