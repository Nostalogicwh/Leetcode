class Solution(object):
    def maxCoins(self, piles):
        piles.sort()

        size = len(piles)
        start = size//3
        res=0    
        for i in range(start,size,2):
            res+=piles[i]

        return res