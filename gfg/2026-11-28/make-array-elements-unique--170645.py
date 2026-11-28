class Solution:
    def minIncrements(self, arr):
        arr.sort()
        moves = 0
        next_free = arr[0]
        for x in arr:
            if x < next_free:
                moves += next_free - x
                next_free += 1
            else:
                next_free = x + 1
        return moves
