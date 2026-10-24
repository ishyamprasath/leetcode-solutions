class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: return [next((y for y in nums2[nums2.index(x)+1:] if y>x),-1) for x in nums1]
