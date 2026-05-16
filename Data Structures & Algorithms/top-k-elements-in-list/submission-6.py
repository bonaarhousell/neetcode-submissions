class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 1
        n = 2
        l = k

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        newNums = set()
        for key, value in freq.items():
            for i in range(k):
                if value > 1:
                    newNums.add(key)
            if len(nums) <= 1:
                return nums
            
        print(newNums) 
        
        return list(newNums) 
            