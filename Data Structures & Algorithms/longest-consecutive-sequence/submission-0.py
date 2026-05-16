class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nums = set(nums)
        base = min(nums)
        res = 1

        for n in nums:
            if base + 1 != n:
                continue
            else:
                res += 1
                base = n


        return res       