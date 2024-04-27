# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr and curr.next:
            next = curr.next
            rest = next.next
            next.next = curr
            curr.next = rest
            head = next
        if head and head.next:
            prev = head.next
            curr = prev.next
            while (prev and curr):
                next = curr.next
                if next:
                    prev.next = next
                    rest = next.next if next.next else None
                    next.next = curr
                    curr.next = rest
                prev = curr
                curr = curr.next
        return head
            
            