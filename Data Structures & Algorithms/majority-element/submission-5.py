class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in range(len(nums)):
            for n in nums:
                if count == 0:
                    res = n
                if res != nums[i]:
                    count -= 1
                else:
                    count += 1

        return res
        
