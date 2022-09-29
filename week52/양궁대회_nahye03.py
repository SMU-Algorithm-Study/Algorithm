from itertools import combinations_with_replacement as cwr
from collections import Counter

def solution(n, info):
    answer = [-1]
    info = info[::-1]
    max_score = 0

    for i in cwr(range(0,len(info)), n):
        diff = 0
        tmp = [0]*len(info)
        c = Counter(i)

        for j in range(len(info)):
            if info[j]<c[j]: #라이언 승
                diff += j
            elif info[j]!=0: #어피치 승
                diff -= j
            tmp[j] = c[j]

        if diff>max_score:
            max_score=diff
            answer = tmp

    return answer[::-1]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))