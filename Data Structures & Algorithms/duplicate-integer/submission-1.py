class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = {}
        for n in nums:
            if n in tmp:
                return True
            
            tmp[n] = 1
        return False

            
                