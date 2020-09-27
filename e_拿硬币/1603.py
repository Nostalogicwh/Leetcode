class Solution:
    def minCount(self, coins: List[int]) -> int:
        sum = 0
        for i in coins:
            if i % 2 == 0:
                sum = sum + i // 2
            else:
                sum = sum + i // 2 + 1
        return sum