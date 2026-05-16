class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        newNums = set()
        for f in freq:
            if freq[f] > 1:
                k += 1
                newNums.add(f)
            else:
                k -= 1

        return list(newNums)