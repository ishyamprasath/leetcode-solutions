# LeetCode 2747. Count Zero Request Servers (POD 2026-11-06)
from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time; answer queries in increasing time with a sliding window.
        logs_sorted = sorted(logs, key=lambda item: item[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        freq: dict[int, int] = defaultdict(int)
        active = 0
        left = 0
        right = 0
        m = len(logs_sorted)

        for qi in order:
            q = queries[qi]
            # Include all requests with time <= q.
            while right < m and logs_sorted[right][1] <= q:
                sid = logs_sorted[right][0]
                if freq[sid] == 0:
                    active += 1
                freq[sid] += 1
                right += 1
            # Drop requests with time < q - x (window is [q - x, q]).
            start = q - x
            while left < right and logs_sorted[left][1] < start:
                sid = logs_sorted[left][0]
                freq[sid] -= 1
                if freq[sid] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2]
    assert s.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]) == [0, 1]
    # Edge: no logs
    assert s.countServers(2, [], 1, [2, 5]) == [2, 2]
    # Edge: all servers hit
    assert s.countServers(1, [[1, 1]], 0, [1]) == [0]
    print("ok")
