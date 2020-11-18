class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        L = len(gas)
        for i in range(L):
            ret = 0
            for j in range(i, L+i):
                if j >= L:
                    j -= L
                ret += gas[j]-cost[j]
                if ret < 0:
                    break
            else:
                return i
        return -1