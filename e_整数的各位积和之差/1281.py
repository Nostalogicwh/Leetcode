class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mult = 1
        num = []
        while n:
            num.append(n % 10)
            n = n // 10

        num.reverse()
        for i in num:
            sum += i
            mult = mult * i
        return mult - sum