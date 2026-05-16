class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = []
        for i in range(k):
            if nums[i] in res:
                print("try if")
                return False
             
            res.append(nums[i])

            if nums[i] > k:
                return False

        
        return True