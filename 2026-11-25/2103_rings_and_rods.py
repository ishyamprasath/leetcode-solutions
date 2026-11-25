class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        for i in range(0, len(rings), 2):
            rods[rings[i + 1]].add(rings[i])
        return sum(1 for colors in rods.values() if len(colors) == 3)
