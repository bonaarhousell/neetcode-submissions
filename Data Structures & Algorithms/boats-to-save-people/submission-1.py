class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len (people) - 1

        res = 0
        people.sort()
        print(people)
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
            elif people[r] == limit - 1:
                res += 1
                r -= 1
            elif people[l] > 2 and limit > 3:
                res  += 1
                l += 1
            else:
                r -= 1
                l += 1
            
        return res