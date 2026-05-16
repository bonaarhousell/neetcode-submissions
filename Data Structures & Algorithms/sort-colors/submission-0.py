class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        r = len(nums) - 1
        l = 1
        while l <= r:
            if nums[i] > nums[l]:
                nums[i],nums[l] = nums[l],nums[i]
                l += 1
                i += 1
            elif nums[i] < nums[l]:
                l += 1
                i += 1
            else:
                l += 1
                i += 1

        r2 = len(nums) - 1
        k = 0
        j = 1
        while j <= r2:
            if nums[k] > nums[j]:
                nums[k],nums[j] = nums[j], nums[k]
                k += 1
                j += 1
            else:
                k += 1
                j += 1
