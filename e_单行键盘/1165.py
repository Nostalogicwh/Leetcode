class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        a = 0
        b = 0
        for i in word:
            for j in range(len(keyboard)):
                if i == keyboard[j]:
                    a =  a + abs(j - b)
                    b = j
        return a