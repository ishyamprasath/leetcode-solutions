# Partition Array Into Three Parts With Equal Sum — Easy — https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        parts = 0
        current = 0
        for value in arr:
            current += value
            if current == target:
                parts += 1
                current = 0
                if parts == 3:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    assert s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]) is True
    assert s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]) is False
    assert s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) is True
    print("samples passed")
