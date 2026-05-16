class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums) - 1
        i = 0
        n2 = len(nums) - 1
        l = 0
        r = 1
        while i < n:
            if nums[i] >= nums[n]:
                nums[i], nums[n] = nums[n],nums[i]
                
            i += 1
            n -= 1
        
        while r <= n2:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
            else:
                r += 1
                l += 1

        return nums

            