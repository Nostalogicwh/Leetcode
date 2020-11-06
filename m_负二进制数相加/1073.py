class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1 
        res, carry = [], 0 
        arr1, arr2 = arr1[::-1], arr2[::-1]
        ## 原始arr1 补充前置0使其与arr2等长
        arr1.extend([0] * (len(arr2) - len(arr1)))

        for i in range(len(arr1)):
            cur = arr1[i] + arr2[i] + carry
            if cur > 1:
                carry = -1
                cur -= 2
            elif cur < 0:
                carry = 1
                cur += 2
            else:
                carry = 0
            res.append(cur)

        res.extend([1, 1]) if carry != 0 else 0
        ## 去掉前置0
        while len(res) >= 2 and res[-1] == 0: 
            res.pop()
        return res[::-1]