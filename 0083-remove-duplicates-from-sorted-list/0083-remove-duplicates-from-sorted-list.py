# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        sentinel=ListNode()
        tail=sentinel
        
        curr=head
        
        while(curr.next):
            succ=curr.next
            curr.next=None
            if(curr.val!=succ.val):
                tail.next=curr
                tail=curr
            curr=succ
        tail.next=curr
        head=sentinel.next
        return head