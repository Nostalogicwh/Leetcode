class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int):
        # 要求的是非重叠且连续的两个子数组
        # 所以有两种情况，要么L在前，M在后；要么M在前，L在后
        # 所以在遍历的过程中分别计算留足余量后的最大值
        # 加起来的最大值就是前一个最大值加上后面存在的各种值
        for i in range(1, len(A)):
            A[i] += A[i-1]

        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]

        for i in range(L+M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            # 分别包括了 L 个子数组在前和 M 个子数组在前
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res