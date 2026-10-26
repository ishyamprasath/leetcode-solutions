class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {name: i for i, name in enumerate(list1)}
        best = float('inf')
        result = []
        for j, name in enumerate(list2):
            if name in index1:
                total = index1[name] + j
                if total < best:
                    best = total
                    result = [name]
                elif total == best:
                    result.append(name)
        return result
