class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = []
        last_added = -1
        for j in range(n):
            if nums[j] == key:
                start = max(last_added + 1, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    result.append(i)
                last_added = max(last_added, end)
        return result
