# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head3=ListNode()
        
        
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list2 and not list1:
            return None
        
        if list1.val<=list2.val:
            head3.val=list1.val
            curr3=head3
            list1=list1.next
        else:
            head3.val=list2.val
            curr3=head3
            list2=list2.next
       
        
        while(list1 and list2):
            if list1.val<list2.val:
                curr3.next=list1
                curr3=list1
                list1=list1.next
               
            else:
                curr3.next=list2
                curr3=list2
                list2=list2.next
           
        if(list1 and not list2):
            curr3.next=list1
        if list2 and not list1:
            curr3.next=list2
        
        
       
        
        return head3
                
                
            