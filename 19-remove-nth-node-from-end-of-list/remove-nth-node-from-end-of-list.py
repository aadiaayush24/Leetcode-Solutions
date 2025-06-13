# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode(val='-1')
        dummy.next = head

        back = dummy
        ahead = dummy
        prev = None

        for _ in range(n+1):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            back = back.next

        back.next = back.next.next
        
        return dummy.next