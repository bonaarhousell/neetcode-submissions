class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1

        nums.sort()
    
        prev = 0
        for num in nums:
            if num - 1 > 0 and num - 1 != prev:
                res = num - 1
                while res != prev:
                    res -= 1
                
                return res + 1
            prev = num
        return prev + 1