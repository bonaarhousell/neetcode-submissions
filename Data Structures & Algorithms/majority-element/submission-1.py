class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i, n in enumerate(nums):
            if n in freq:
                freq[n] = i + 1
            freq[n] = i
            print(freq)
        
        majority = 0
        for maj in freq:
            if freq[maj] > majority:
                majority = maj
        print (majority)
        return majority