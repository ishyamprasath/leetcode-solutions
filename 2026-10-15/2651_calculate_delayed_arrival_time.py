# LeetCode 2651. Calculate Delayed Arrival Time
# Arrival wraps around a 24-hour clock.


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
