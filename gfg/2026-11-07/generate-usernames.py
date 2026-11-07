class Solution:
    def generateUsernames(self, arr):
        reserved = set(arr)
        assigned = set()
        next_suffix = {}
        result = []
        for name in arr:
            if name not in assigned:
                assigned.add(name)
                result.append(name)
            else:
                suffix = next_suffix.get(name, 1)
                candidate = name + str(suffix)
                while candidate in reserved or candidate in assigned:
                    suffix += 1
                    candidate = name + str(suffix)
                assigned.add(candidate)
                result.append(candidate)
                next_suffix[name] = suffix + 1
        return result
