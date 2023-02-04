# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel=ListNode()
        tail=sentinel
        
        prev=None
        curr=head
        
        while(head):
            
            count1,count2=0,0
            while(curr and count1<m):
                prev=curr
                curr=curr.next
                count1+=1
            prev.next=None
            tail.next=head
            tail=prev
            
            
            while(curr and count2<n):
                prev=curr
                curr=curr.next
                count2+=1
            head=curr
        head=sentinel.next
        return head