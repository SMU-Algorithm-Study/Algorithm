def solution(d, budget):
    answer = 0
    d_ = sorted(d) #오름차순 정렬

    sum_d = 0
    for i in range(len(d)):
        sum_d += d_[i]
        if sum_d > budget:
            break
        answer += 1

    return answer