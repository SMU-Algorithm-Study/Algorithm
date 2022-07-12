def solution(id_list, report, k):
    answer = []
    id_table = {} #유저 id : 유저가 신고한 id
    cnt_table = {} # 신고받은 id : 신고 횟수
    stop_id = [] #정지 id

    for i in id_list:
        id_table[i]=[]
        cnt_table[i] = 0

    for i in report:
        id_table[i.split()[0]].append(i.split()[1])

    for key,v in id_table.items():
        if v:
            id_table[key] = set(v)
            for i in set(v):
                cnt_table[i] += 1

    for i in id_list:
        if cnt_table[i] >= k:
            stop_id.append(i)

    for i in id_list:
        answer.append(len(list(set(id_table[i]) & set(stop_id))))

    print(id_table)
    print(cnt_table)
    print(answer)

    return answer

#다른 방법
# def solution(id_list, report, k):
#     answer = [0]*len(id_list)
#     reports = {x:0 for x in id_list}
#
#     for r in set(report):
#         reports[r.split()[1]]+=1
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] +=1
#
#     return answer