# Add Number Linked Lists
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/add-two-numbers-represented-by-linked-lists
class Solution:
    def addTwoLists(self, head1, head2):
        a, b = [], []
        while head1:
            a.append(head1.data)
            head1 = head1.next
        while head2:
            b.append(head2.data)
            head2 = head2.next
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = None
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += a[i]
                i -= 1
            if j >= 0:
                total += b[j]
                j -= 1
            node = Node(total % 10)
            node.next = result
            result = node
            carry = total // 10
        while result.next and result.data == 0:
            result = result.next
        return result
