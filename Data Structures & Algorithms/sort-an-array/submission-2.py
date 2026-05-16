class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        i = 0

        while i <= r:
        
            if nums[i] > nums[r]:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            
            i += 1
        
        n = len(nums) // 2
        j = len(nums) - 1

        while j >= n:
            if nums[n] > nums[j]:
                nums[n] , nums[j] = nums[j], nums[n]
                j -= 1
                n -= 1

            n += 1

        return nums