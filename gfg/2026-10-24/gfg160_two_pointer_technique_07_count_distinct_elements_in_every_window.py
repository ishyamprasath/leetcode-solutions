class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        result = []
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            if i >= k:
                old = arr[i - k]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
            if i >= k - 1:
                result.append(len(freq))
        return result
