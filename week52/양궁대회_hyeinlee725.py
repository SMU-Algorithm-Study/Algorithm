from itertools import combinations_with_replacement as cwr
def solution(n, info):
    answer = [-1]
    max_gap = -1
    len_info = len(info)
    for comb in cwr(range(len_info), n):
        apeach = 0
        ryan = 0
        tmp = [0 for _ in range(len_info)]
        
        for i in comb:
            tmp[10 - i] += 1
        for idx in range(0, len_info):
            if info[idx] == tmp[idx] == 0:
                continue
            elif info[idx] >= tmp[idx]:
                apeach += 10 - idx
            else:
                ryan += 10 - idx
        if ryan > apeach:
            gap = ryan - apeach
            if max_gap < gap :
                max_gap = gap
                answer = tmp
    return answer
