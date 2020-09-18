class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        judge = []
        for i in candies:
            judge.append(i + extraCandies >= maxnum)
        return judge