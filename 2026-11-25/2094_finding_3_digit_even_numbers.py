class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        have = Counter(digits)
        result = []
        for num in range(100, 1000, 2):
            need = Counter(map(int, str(num)))
            if all(have[d] >= c for d, c in need.items()):
                result.append(num)
        return result
