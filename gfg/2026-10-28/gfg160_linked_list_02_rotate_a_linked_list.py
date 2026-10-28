# Rotate a Linked List
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/rotate-a-linked-list
class Solution:
    def rotate(self, head, k):
        if not head or not head.next:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        prev = head
        for _ in range(k - 1):
            prev = prev.next
        new_head = prev.next
        prev.next = None
        tail.next = head
        return new_head
