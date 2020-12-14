class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a = 0
        b = 0
        p = [[0,0]]
        for i in range(len(path)):
            if path[i] == 'N':
                a += 1
                if [b,a] in p:
                    return True
                else:
                    p.append([b,a])
            if path[i] == 'E':
                b += 1
                if [b,a] in p:
                    return True
                else:
                    p.append([b,a])
            if path[i] == 'S':
                a -= 1
                if [b,a] in p:
                    return True
                else:
                    p.append([b,a])
            if path[i] == 'W':
                b -= 1
                if [b,a] in p:
                    return True
                else:
                    p.append([b,a])
        return False