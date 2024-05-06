# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        llist = []
        curr = head
        while curr:
            llist.append(curr.val)
            curr = curr.next
        stack = []
        while llist:
            n = llist.pop()
            if stack and stack[-1] > n:
                pass
            else:
                stack.append(n)
        if stack:
            head = ListNode(stack.pop())
            curr = head
            while stack:
                curr.next = ListNode(stack.pop())
                curr = curr.next
            return head
        else:
            return None
            
            

                        
