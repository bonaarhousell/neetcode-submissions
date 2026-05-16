class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0 ) + 1

        newNums = []
        
        for f in freq:
            if freq[f] >= k:
                newNums.append(f)
                

        return newNums