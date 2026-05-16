class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        i = 0

        while k < n:
            nums[i] = nums[k]
            while k < n and nums[k] == nums[i]:
                k += 1

            i += 1

        return i