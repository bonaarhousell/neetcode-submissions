class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, n in enumerate(nums):
            test = target - n
            if test in result:
                return [result[test], i]
            result[n] = i

            

                    
