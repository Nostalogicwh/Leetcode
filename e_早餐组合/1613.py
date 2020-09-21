class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        ans = 0
        arr = [0 for i in range(x+1)]
        
        for sta in staple:
            if sta < x:
                arr[sta] += 1
        
        for i in range(2, x):
            arr[i] += arr[i-1]
        
        for drink in drinks:
            lt = x - drink
            if lt <= 0:
                continue
            ans += arr[lt]
            
        return ans % (10 ** 9 + 7)