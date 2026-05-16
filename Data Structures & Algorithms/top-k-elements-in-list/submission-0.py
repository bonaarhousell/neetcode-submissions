class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0 ) + 1

        newNums = []
        k = 0
        for f in freq:
            if freq[f] > 1:
                newNums.append(f)
                k += 1

        return newNums