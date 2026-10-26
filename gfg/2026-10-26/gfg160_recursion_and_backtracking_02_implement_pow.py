class Solution:
    def power(self, b: float, e: int) -> float:
        # Fast exponentiation (square and multiply)
        if e < 0:
            b = 1.0 / b
            e = -e
        result = 1.0
        while e > 0:
            if e & 1:
                result *= b
            b *= b
            e >>= 1
        return result
