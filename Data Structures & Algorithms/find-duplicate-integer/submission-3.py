class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] 
            if slow == fast:
                break

        slowly = 0
        while True:
            slow = nums[slow]
            slowly = nums[slowly]
            if slow == slowly:
                return slow

        
