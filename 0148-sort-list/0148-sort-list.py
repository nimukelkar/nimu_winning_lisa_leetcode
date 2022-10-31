# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergetwo(self,list1,list2):
        sentinel=ListNode()
        curr=sentinel
        
        while(list1 and list2):
            if list1.val<=list2.val:
                curr.next=list1
                curr=list1
                list1=list1.next
            else:
                curr.next=list2
                curr=list2
                list2=list2.next
        if list1 and not list2:
            curr.next=list1
        if list2 and not list1:
            curr.next=list2
            
        head3=sentinel.next     
        return head3
    
        '''if not list1 and not list2:
            print("In here 1")
            return
        if not list1 and list2:
            print("In here 2")
            return list2
        if not list2 and list1:
            print("In here 3")
            return list1
        head3=ListNode()
        if list1.val<=list2.val:
            head3.val=list1.val
            curr=head3
            list1=list1.next
        else:
            head3.val=list2.val
            curr=head3
            list2=list2.next
        while(list1 and list2):
            if list1.val<=list2.val:
                curr.next=list1
                curr=list1
                list1=list1.next
            else:
                curr.next=list2
                curr=list2
                list2=list2.next
        if list1 and not list2:
            curr.next=list1
        if list2 and not list1:
            curr.next=list2
        return head3'''
    
    def findmid(self,head):
        slow=head
        fast=head
        
        while(fast.next and fast.next.next):
                fast=fast.next.next
                slow=slow.next
        
        '''while(fast.next):
            
            if not fast.next:
                break
            if fast.next.next:
                fast=fast.next.next
                slow=slow.next
            else:
                break'''
        
          
           
        return slow
    
    def recurse(self,head):
        if not head.next or not head:
            return head
        slow=self.findmid(head) 
        head_right=slow.next
        slow.next=None
        
        head=self.recurse(head)
        head_right=self.recurse(head_right)
        ans=self.mergetwo(head,head_right)
        return ans
        
        
        
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ans=self.recurse(head)
        return ans
        
        
        
        
        
        
        
        
        