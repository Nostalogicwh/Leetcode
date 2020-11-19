class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        minnum = str(min(A))
        num = 0
        for i in range(len(minnum)):
            num += int(minnum[i])
        if num % 2 == 0:
            return 1
        else:
            return 0