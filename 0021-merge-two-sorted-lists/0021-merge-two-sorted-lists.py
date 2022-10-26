# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        head3=ListNode()
        
        
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list2 and not list1:
            return None
        if curr1.val<=curr2.val:
            head3.val=curr1.val
            curr3=head3
            curr1=curr1.next
        else:
            head3.val=curr2.val
            curr3=head3
            curr2=curr2.next
       
        
        while(curr1 and curr2):
            if curr1.val<curr2.val:
                p=ListNode()
                p.val=curr1.val
                curr3.next=p
                curr3=p
                curr1=curr1.next
               
            else:
                p=ListNode()
                p.val=curr2.val
                curr3.next=p
                curr3=p
                curr2=curr2.next
                
        if(curr1 and not curr2):
            curr3.next=curr1
        if curr2 and not curr1:
            curr3.next=curr2
        
        
       
        
        return head3
                
                
            