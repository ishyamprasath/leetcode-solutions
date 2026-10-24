class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int: return sum(min(b-a,duration) for a,b in zip(timeSeries,timeSeries[1:]))+duration
