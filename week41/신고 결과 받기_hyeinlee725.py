def solution(id_list, report, k):
    answer = [0] * len(id_list) # 처리 결과 메일을 받은 횟수
    rep = {x : 0 for x in id_list} # 신고 횟수
    set_rep = set(report)

    for i in set_rep:
        rep[i.split()[1]] += 1 # 신고횟수 추가

    for j in set_rep:
        # k번 이상 신고 - 받을 메일 추가
        if rep[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])] += 1

    return answer
