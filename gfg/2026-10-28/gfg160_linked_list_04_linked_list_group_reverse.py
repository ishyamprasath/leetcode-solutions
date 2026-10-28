# Linked List Group Reverse
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/reverse-a-linked-list-in-groups-of-given-size
class Solution:
    def reverseKGroup(self, head, k):
        prev_tail = None
        new_head = None
        cur = head
        while cur:
            group_head = cur
            prev = None
            count = 0
            while cur and count < k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                count += 1
            if new_head is None:
                new_head = prev
            else:
                prev_tail.next = prev
            prev_tail = group_head
        return new_head
