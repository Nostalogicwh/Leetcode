class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a = 0   #5
        b = 0   #10
        for i in bills:
            if i == 5:
                a += 1
            if i == 10:
                if a >= 1:
                    a -= 1
                    b += 1
                else:
                    return False
            if i == 20:
                if b >= 1 and a >= 1:
                    a -= 1
                    b -= 1
                elif a >= 3:
                    a -= 3
                else:
                    return False
        return True