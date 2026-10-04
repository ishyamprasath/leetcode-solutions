# 83. Remove Duplicates from Sorted List (Easy)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head): return head if not head or not head.next else (setattr(head, 'next', self.deleteDuplicates(head.next)) or (head.next if head.val == head.next.val else head))
