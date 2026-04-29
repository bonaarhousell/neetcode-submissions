class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        lenght = m + n
        r = len(nums2) - 1
        i = 0
        while i <= r:
            nums1[m] = nums2[i]

            m += 1
            i += 1

        nums1.sort()
            