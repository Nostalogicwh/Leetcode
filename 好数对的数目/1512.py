class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hs = {}
        count = 0
        for i in nums:
            if i not in hs.keys():
                hs[i]=1
            else:
                hs[i]+=1
        for v in hs.values():
            if v!=1:#剔除只出现一次的数字，可以减少很多多余运算，以提高性能
                count += v*(v-1)//2#结果一定是整数，但用‘/’会返回浮点，故使用整除‘//’
        return count
