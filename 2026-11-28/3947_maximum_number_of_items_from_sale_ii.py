class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_factor = max(f for f, _ in items)
        count = [0] * (max_factor + 1)
        for f, _ in items:
            count[f] += 1

        # multiples[f] = number of items whose factor is a multiple of f
        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if count[f]:
                multiples[f] = sum(count[m] for m in range(f, max_factor + 1, f))

        # The first d_i copies of item i are each worth 2 (itself + one free copy),
        # where d_i = number of other items whose factor is a multiple of factor_i.
        # Any other copy is worth 1, and the cheapest way to get a value-1 copy
        # costs the minimum price. A value-2 copy only helps if price < 2 * cheapest.
        cheapest = min(p for _, p in items)
        offers = sorted((p, multiples[f] - 1) for f, p in items if multiples[f] > 1 and p < 2 * cheapest)

        total = 0
        money = budget
        for price, copies in offers:
            take = min(copies, money // price)
            if take == 0:
                break
            total += 2 * take
            money -= take * price
        return total + money // cheapest
