class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            freq[n] = 1
        
        majority = 0
        for maj in freq:
            if maj > majority:
                majority = maj
        print (maj)
        return majority