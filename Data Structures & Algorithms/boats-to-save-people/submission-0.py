class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len (people) - 1

        res = 0
        people.sort()

        while l <= r:
            if people[r] == limit:
                res += 1
                r -= 1
            elif people[l] + people[r] == limit:
                res += 1
                r -= 1
                l += 1
            elif people[l] == limit - 1:
                res += 1
                l += 1
            
        return res