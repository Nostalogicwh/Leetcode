class Solution:
    def findIntegers(self, num: int) -> int:
        num += 1 #找比num+1小的符合条件的所有数字，这样包含了num
        prev, curr = 1, 1  #curr = f(0)，每次循环变为f(1), f(2)...
        ret = 0
        while num:
            if num & 3 == 3: #如果是0b11结尾，清除之前结果
                ret = 0
            if num & 1: #如果是0b1结尾，加上f()
                ret += curr
            num >>= 1 # 右移一位
            prev, curr = curr, prev + curr # 斐波那契额数列计算
        return ret