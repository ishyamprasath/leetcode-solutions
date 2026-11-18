class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        start = {piece[0]: piece for piece in pieces}
        i = 0
        while i < len(arr):
            piece = start.get(arr[i])
            if piece is None or arr[i:i + len(piece)] != piece:
                return False
            i += len(piece)
        return True
