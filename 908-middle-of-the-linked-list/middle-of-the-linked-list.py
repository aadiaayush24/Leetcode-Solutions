# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        countNodes = 0
        travel = head
        while travel:
            countNodes += 1
            travel = travel.next
        travel = head
        mid = countNodes//2
        while travel:
            if (mid == 0):
                return travel
            mid -= 1
            travel = travel.next
        return None