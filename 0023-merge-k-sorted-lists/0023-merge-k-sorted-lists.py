# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergetwo(self,list1,list2):
        if not list1 and not list2:
            return
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        
        head3=ListNode()
        if(list1.val<=list2.val):
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
        #print("curr3.val",curr.val)    
        return head3
    
    def recurse(self,lists,low,high):
        if low>=high:
            return 
        mid=(low+high)//2
        self.recurse(lists,low,mid)
        self.recurse(lists,mid+1,high)
        lists[low]=self.mergetwo(lists[low],lists[mid+1])
        
        
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==[]:
            return
        low=0
        high=len(lists)-1
        self.recurse(lists,low,high)
        return lists[low]