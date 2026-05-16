class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        while i < n:
            diff = target - numbers[0]
            if diff == numbers[i]:
                return [numbers[0], diff]
                i += 1
            i += 1