class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            # 排序后加入字典
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        # 计算答案
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans