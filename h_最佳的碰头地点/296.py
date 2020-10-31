class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        people = []
        rowl = len(grid)    #行
        coll = len(grid[0]) #列
        for i in range(rowl):
            for j in range(coll):
                if grid[i][j] == 1:
                    people.append([i,j])
        res_row = 1000000
        res_col = 1000000
        for i in range(rowl):
            ans = 0
            for person in people:
                ans = ans + abs(person[0]-i)
            if ans < res_row:
                res_row = ans
        for i in range(coll):
            ans = 0
            for person in people:
                ans = ans + abs(person[1]-i)
            if ans < res_col:
                res_col = ans

        return res_row+res_col