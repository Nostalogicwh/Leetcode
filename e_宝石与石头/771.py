class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for i in S:
            if i in J:
                sum += 1
        return sum