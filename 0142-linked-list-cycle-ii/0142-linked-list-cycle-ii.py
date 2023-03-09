# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return None
        slow=head
        fast=head.next
        
        while(fast.next is not None and fast.next.next is not None and slow!=fast):
            slow=slow.next
            fast=fast.next.next
        if (slow==fast):
            print(slow.val)
            slow=slow.next
            fast=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow
        else:
            return None