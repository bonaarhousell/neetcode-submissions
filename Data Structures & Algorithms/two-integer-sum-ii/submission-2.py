class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = 1
        n = len(numbers) - 1

        while l < n:
            

            if numbers[l] + numbers[r] == target:
                return [l + 1,r + 1]

            while r == n:
                l += 1
                if numbers[l] + numbers[r] == target:
                    return [l + 1,r + 1]

            r += 1
