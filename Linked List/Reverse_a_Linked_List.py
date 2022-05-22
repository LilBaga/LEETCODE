# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: 
            return None
        if not head.next:
            return head

        curr= head.next
        prev= head;
        nexti = None;
        head.next = None
        
        while curr:
            nexti= curr.next
            curr.next = prev
            
            prev = curr
            
            curr = nexti
        
        return prev
        
