class Solution:
    def checkRecord(self, s: str) -> bool:
        # Eligible if fewer than 2 absences and no 3 consecutive lates.
        return s.count("A") < 2 and "LLL" not in s
