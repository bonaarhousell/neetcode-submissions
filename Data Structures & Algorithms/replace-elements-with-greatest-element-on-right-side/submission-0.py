class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i + 1 == len(arr):
                arr[i] = -1
                break
            highest = max(arr[i + 1:])
            arr[i] = highest

        return arr