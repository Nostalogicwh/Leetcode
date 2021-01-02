class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        m = len(flowerbed)
        for i in range(m):
            # 判断当前及左右位置是否种植了花
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i+1 < m and flowerbed[i+1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False