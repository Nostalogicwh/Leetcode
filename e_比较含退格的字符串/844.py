class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        charS = []
        charT = []
        for i in S:
            if i != '#':
                charS.append(i)
            else:
                if charS:
                    charS.pop()
        for i in T:
            if i != '#':
                charT.append(i)
            else:
                if charT:
                    charT.pop()
        charS = ''.join(charS)
        charT = ''.join(charT)

        if charS == charT:
            return True
        else:
            return False