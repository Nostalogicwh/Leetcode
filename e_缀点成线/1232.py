class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0
        for i in range(2, len(coordinates)):
            temp_dx, temp_dy = coordinates[i][0] - x0, coordinates[i][1] - y0
            if dx * temp_dy != dy * temp_dx:
                return False
        return True