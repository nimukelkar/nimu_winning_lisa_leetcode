# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #Modify the list in place.
        sentinel=ListNode(0,head)
        prev=sentinel
        curr=head
        
        while(curr):
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        head=sentinel.next
        return head
        