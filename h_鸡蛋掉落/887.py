class Solution:
    def superEggDrop(self, K, N): 
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1): 
            for j in range(1, K + 1):
                f[i][j] = f[i - 1][j - 1] + 1 + f[i - 1][j]
                if f[i][K] >= N:
                    return i
