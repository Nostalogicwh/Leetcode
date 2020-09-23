class Solution:
    def shortestSubarray(self, A: [int], K: int) -> int:
        def binarySearch(ar, target):
            # ar[:l] <= target
            l, r = 0, len(ar)
            while l < r:
                mid = (l + r) >> 1
                if ar[mid][0] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        stack = [(0, -1)]  # 前缀和单调递增栈，栈中元素为（前缀和，对应数组索引）
        sums = 0
        result = 1 << 31
        for i, num in enumerate(A):
            sums += num
            while len(stack) > 0 and stack[-1][0] >= sums:
                stack.pop()
            idx = binarySearch(stack, sums - K)
            if idx > 0:
                result = min(result, i - stack[idx-1][1])
            stack.append((sums, i))

        return result if result != 1 << 31 else -1