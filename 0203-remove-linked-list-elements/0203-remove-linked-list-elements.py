# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
       
        if not head:
            return None
        curr=head
        
        while(curr.val==val):
            curr=curr.next
            if not curr: 
                break
                
        head=curr
        
        if not head:
            return None
       
          
        while(curr.next):
            while(curr.next.val==val):
                curr.next=curr.next.next
                if( not curr.next):
                    break
            
            curr=curr.next
            if not curr:
                break
        
            
        
        return head
        