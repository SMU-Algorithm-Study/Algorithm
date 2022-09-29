from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    score_gap = 0
    for combi in combinations_with_replacement(range(11), n):
        lion = 0
        apeach = 0
        lion_score = [0] * 11

        for i in combi:
            lion_score[10-i] += 1

        for i in range(11):
            if lion_score[i] == 0 and info[i] == 0:
                continue
            elif lion_score[i]>info[i]:
                lion += (10-i)
            else:
                apeach += (10 - i)
        if lion > apeach and lion-apeach > score_gap:
            score_gap = lion-apeach
            answer = lion_score

    return answer


print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))