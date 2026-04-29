class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = []
        for n in nums:
            if n != val:
                num.append(n)

        for i in range(len(num)):
            nums[i] = num[i]

        return len(num)