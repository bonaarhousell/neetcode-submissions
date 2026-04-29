class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, x in enumerate(nums):
            targets = target - x
            if targets in result:
                return [result[targets], i]
            result[x] = i
        return []