class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0

        for n in newSet:
            if (n - 1) not in newSet:
                lenght = 1
                while n + lenght in newSet:
                    lenght += 1
                longest = max(lenght, longest)

        return longest