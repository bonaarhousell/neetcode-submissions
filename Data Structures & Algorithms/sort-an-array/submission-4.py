class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sortah():
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        sortah()
        return nums