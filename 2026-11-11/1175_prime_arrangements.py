import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        for value in range(2, n + 1):
            if all(value % divisor for divisor in range(2, int(value ** 0.5) + 1)):
                prime_count += 1
        other_count = n - prime_count
        mod = 10**9 + 7
        return (math.factorial(prime_count) * math.factorial(other_count)) % mod
