class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        num1 = 0
        num2 = 0
        while num2 < len(typed):
            if num1 < len(name) and name[num1] == typed[num2]:
                num1 += 1
                num2 += 1
            elif num2 > 0 and typed[num2] == name[num1 - 1]: 
                num2 += 1
            else:
                return False
        return num1 == len(name)