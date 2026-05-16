class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums) - 1
        i = 0
        k = 1

        while k <= n:
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k],nums[i]
                k += 1
                i += 1
            else:
                i += 1
                k += 1

        i2 = len(nums) - 1
        k2 = len(nums) - 2
    
        while k2 >= 0:
            if nums[i2] < nums[k2]:
                nums[k2],nums[i2] = nums[i2], nums[k2]
                k2 -= 1
                i2 -= 1
            else:
                i2 -= 1
                k2 -= 1

        n2 = len(nums) - 1
        l = 0
        r = 1

        while r <= n2:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
            else:
                r += 1
                l += 1
        
    
        return nums

            