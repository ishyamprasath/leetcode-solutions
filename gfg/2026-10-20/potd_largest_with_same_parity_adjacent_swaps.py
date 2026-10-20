# GFG POTD 2026-10-20: Largest with Same Parity Adjacent Swaps
class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # Only adjacent elements of the same parity can be swapped, so each
        # maximal run of equal parity can be rearranged freely.
        # Sort every such run in descending order.
        n = len(arr)
        result = []
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] % 2 == arr[i] % 2:
                j += 1
            result.extend(sorted(arr[i:j], reverse=True))
            i = j
        return result
