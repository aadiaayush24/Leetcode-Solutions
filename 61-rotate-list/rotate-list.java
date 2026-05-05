/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head==null) {
            return null;
        }
        ListNode dummy = new ListNode(-101);
        int n=0;
        ListNode cntNode=head;

        while (cntNode!=null) {
            n++;
            cntNode=cntNode.next;
        }
        k=k%n;
        if(k==0) return head;

        ListNode iter=head;
        int c=1;

        while (c!=(n-k)) {
            iter=iter.next;
            c++;
        }

        ListNode newHead=iter.next, newTail=iter.next;
        iter.next=null;
        while(newTail.next!=null) {
            newTail=newTail.next;
        }
        dummy.next=newHead;
        newTail.next=head;

        return dummy.next;
    }
}