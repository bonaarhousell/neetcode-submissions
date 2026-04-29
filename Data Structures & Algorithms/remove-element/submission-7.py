class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) 

        i = 0
        k = 0

        while k < n and i < n:
            nums[i] = nums[k]
            while k < n and nums[k] == val:
                k += 1

            if nums[i] != val:
                i += 1
                k += 1

        return i