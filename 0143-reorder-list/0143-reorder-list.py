# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sentinel=ListNode()
        tail=sentinel
        
        
        
        curr=head
        count=0
        
        while(curr):
            count+=1
            curr=curr.next
        
        curr=head
        
        count2=1
        while(count2<count//2):
            count2+=1
            curr=curr.next
            
       
        head2=curr.next
        curr.next=None
        
        #head points to 1 and head2 points to 3.
        #Reverse head2 linked list
        
        prev=None
        current=head2
        while(current):
            future=current.next
            current.next=prev
            prev=current
            current=future
        #print(prev.val)
       
        #merge head and prev
        while(head and prev):
            tail.next=head
            tail=head
            head=head.next
            tail.next=prev
            tail=prev
            prev=prev.next
        if head and not prev:
            tail.next=head
        if not head and prev:
            tail.next=prev
        
        return sentinel.next