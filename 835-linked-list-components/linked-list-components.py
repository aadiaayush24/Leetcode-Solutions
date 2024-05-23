# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums.sort()

        def binary_search(arr, val):
            start = 0
            end = len(arr)-1

            while (start <= end):
                mid = start + (end - start)//2
                if arr[mid] == val:
                    return True
                elif arr[mid] < val:
                    start = mid + 1
                else:
                    end = mid - 1
            return False
        
        curr = head
        comps = 0
        last = False
        while curr:
            if binary_search(nums, curr.val):
                if not last:
                    comps += 1
                last = True 
            else:
                last = False
            curr = curr.next
        return comps
