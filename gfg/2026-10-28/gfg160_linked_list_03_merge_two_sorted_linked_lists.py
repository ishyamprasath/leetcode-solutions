# Merge Two Sorted Linked Lists
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/merge-two-sorted-linked-lists
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        tail = dummy
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        tail.next = head1 if head1 else head2
        return dummy.next
