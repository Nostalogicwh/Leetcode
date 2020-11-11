class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        # 求x位置到y位置的最小旋转步数，就是正向和反向的最小值加上按中心的一步
        def dis(x, y):
            if x > y:
                x, y = y, x
            return min(y - x, x + n - y) + 1

        now_set = [0]  # 记录当前所在的所有可能位，初始在0位
        res = [0]      # 记录对应位置的最优值
        for c in key:
            new_set = []    # 开始计算下一个位置所有可能的位置
            new_res = []    # 对应的最优值
            m = len(now_set)

            for i in range(n):
                if ring[i] == c:
                    new_set.append(i)
                    new_res.append(float('inf'))
                    for j in range(m):
                        new_res[-1] = min(new_res[-1], res[j] + dis(i, now_set[j]))
            
            now_set = new_set
            res = new_res
        return min(res)