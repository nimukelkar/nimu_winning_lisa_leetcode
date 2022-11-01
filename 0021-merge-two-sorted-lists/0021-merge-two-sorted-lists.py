# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinel=ListNode()
        curr=sentinel
        
                      
        while(list1 and list2):
            if list1.val<list2.val:
                curr.next=list1
                curr=list1
                list1=list1.next
               
            else:
                curr.next=list2
                curr=list2
                list2=list2.next
           
        if(list1 and not list2):
            curr.next=list1
        if list2 and not list1:
            curr.next=list2
        
        head=sentinel.next
        return head
        
        
                
            