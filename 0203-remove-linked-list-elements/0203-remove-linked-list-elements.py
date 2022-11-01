# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Building list from scratch
        
        sentinel=ListNode()
        tail=sentinel
        
        curr=head
        
        while(curr):
            succ=curr.next
            curr.next=None
            
            if(curr.val!=val):
                tail.next=curr
                tail=curr
            curr=succ
        head=sentinel.next
        return head
                