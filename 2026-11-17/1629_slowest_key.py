class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        best_key = keysPressed[0]
        best_time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            if duration > best_time or (duration == best_time and key > best_key):
                best_time = duration
                best_key = key
        return best_key
