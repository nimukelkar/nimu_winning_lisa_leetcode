class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1=head
        curr2=head
        l=0
        count=0
        while(curr1):
            l+=1
            curr1=curr1.next
        mid=l//2
        
        while(curr2):
            
            if count==mid:
                return curr2
            else:
                curr2=curr2.next
            count+=1