class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        activities = sorted(zip(finish, start))
        count = 0
        last_end = -1
        for end, begin in activities:
            if begin > last_end:
                count += 1
                last_end = end
        return count
