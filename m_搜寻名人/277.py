# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n):
        if not n:
            return -1
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
            print(celeb) 
        for i in range(n):
            if i == celeb:
                continue
            if not knows(i, celeb) or knows(celeb, i):
                return -1
        return celeb