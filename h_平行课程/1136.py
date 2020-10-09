class Solution:
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        pre_class_cnt = [0] * N
        next_classes = [[] for i in range(N)]
               
        for a, b in relations:
            pre_class_cnt[b - 1] += 1
            next_classes[a - 1].append(b - 1)        

        learn = [i for i in range(N) if pre_class_cnt[i] == 0]

        term = 0
        while learn:
            next_semester = []
            for cur_class in learn:
                for next_class in next_classes[cur_class]:
                    pre_class_cnt[next_class] -= 1
                    if pre_class_cnt[next_class] == 0:
                        next_semester.append(next_class)
            learn = next_semester
            term += 1
        if sum(pre_class_cnt) > 0:
            return -1
        return term