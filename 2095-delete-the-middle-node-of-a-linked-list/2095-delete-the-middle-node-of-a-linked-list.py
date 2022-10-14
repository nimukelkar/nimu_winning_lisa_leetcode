# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1=head
        curr2=head
        l=0
        while(curr1):
            l+=1
            curr1=curr1.next
        if l==1:
            return None
        mid=l//2
        count=0
       
        while(curr2):
            count+=1
            #print("count=",count,"mid=",mid)
            if count==mid:
                #print("Hi")
                curr2.next=curr2.next.next
                
            else:
                curr2=curr2.next
        return head