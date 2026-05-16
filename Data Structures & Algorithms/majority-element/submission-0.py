class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i, n in enumerate(nums):
            if n in freq:
                freq[n] = i + 1
            freq[n] = i

        maj = max(freq)
        return maj