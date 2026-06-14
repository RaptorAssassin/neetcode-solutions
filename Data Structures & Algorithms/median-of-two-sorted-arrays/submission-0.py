class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        if not arr: return 0.0
        middle = len(arr) // 2

        if len(arr) % 2 == 0:
            return (arr[middle] + arr[middle - 1]) / 2
        return arr[middle]