# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr= head
        next= None
        if curr == None:
            return head
        if (curr.next != None):
            next = curr.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = next
            if next == None:
                next = None
            else:
                next = next.next
        return prev