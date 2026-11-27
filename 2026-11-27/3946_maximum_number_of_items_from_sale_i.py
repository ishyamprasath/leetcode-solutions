class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        count = [0] * (max_factor + 1)
        for f, _ in items:
            count[f] += 1

        # free[f] = how many items have a factor that is a multiple of f
        free = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if count[f]:
                free[f] = sum(count[m] for m in range(f, max_factor + 1, f))

        # 0/1 knapsack over "first copy" purchases:
        # the first copy of item i is worth 1 + (free copies it unlocks)
        NEG = float("-inf")
        best = [NEG] * (budget + 1)
        best[0] = 0
        for f, price in items:
            value = 1 + free[f] - 1  # exclude the item itself
            for w in range(budget, price - 1, -1):
                if best[w - price] != NEG and best[w - price] + value > best[w]:
                    best[w] = best[w - price] + value

        # leftover money buys extra copies of the cheapest item (1 each)
        cheapest = min(p for _, p in items)
        answer = 0
        for w in range(budget + 1):
            if best[w] != NEG:
                answer = max(answer, best[w] + (budget - w) // cheapest)
        return answer
