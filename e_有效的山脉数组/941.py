class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        isUp, isDown = False, False

        for i in range(1, len(A)):
            # 上坡
            if (A[i] - A[i-1]) > 0:
                # 已经下过坡了
                if isDown:
                    return False
                isUp = True
            # 下坡
            elif (A[i] - A[i-1]) < 0:
                # 还没上过坡
                if not isUp:
                    return False
                isDown = True
            else:
                return False

        return isUp and isDown