class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        r = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                r += 1
        return r