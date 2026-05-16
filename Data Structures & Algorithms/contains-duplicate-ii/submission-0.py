class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = k - 1

        while l <= r:
            if nums[l] != nums[r]:
                return True

            l += 1
            r -= 1

        return False

