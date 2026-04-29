class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            result[num] = i

        for i, x in enumerate(nums):
            diff = target - x
            if diff in result and result[diff] != i:
                return [i, result[diff]]
        return []