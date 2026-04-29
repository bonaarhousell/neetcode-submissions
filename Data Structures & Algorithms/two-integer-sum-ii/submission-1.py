class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0

        while i < n:
            if numbers[i] + numbers[n - 1] > target:
                n -= 1
            elif numbers[i] + numbers[n - 1] < target:
                i += 1
            else:
                return [i + 1, n ]