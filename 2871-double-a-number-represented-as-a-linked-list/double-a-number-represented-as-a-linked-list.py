# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    sys.set_int_max_str_digits(100000)
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        num = 0
        while curr:
            num = (num*10) + curr.val
            curr = curr.next
        num = list(str(2*num))[::-1]
        curr = head
        prev = None
        while curr:
            value = num.pop()
            curr.val = value
            prev = curr
            curr = curr.next
        while num:
            prev.next = ListNode(num.pop())
        return head