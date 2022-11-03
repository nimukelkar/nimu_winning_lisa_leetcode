# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel=ListNode()
        tail=sentinel
        
        curr=head
        
        while(head):           
            while(curr and curr.val==head.val):
                    curr=curr.next
                     
            if head.next==curr:
                head.next=None
                tail.next=head
                tail=head
            head=curr
            
        head=sentinel.next
        return head