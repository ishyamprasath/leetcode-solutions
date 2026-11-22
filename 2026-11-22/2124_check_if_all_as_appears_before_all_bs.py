from typing import List
from collections import Counter


class Solution:
    def checkString(self, s: str) -> bool:
        # Every 'a' comes before every 'b' exactly when "ba" never appears.
        return "ba" not in s
