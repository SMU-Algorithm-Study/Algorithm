# 22.07.08
# 프로그래머스 - 신고 결과 받기(구현 - 카카오 2022 기출)
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# 내 풀이
def solution(id_list, report, k):
    # 유저 딕셔너리 선언
    user = {}
    for id in id_list:
        user[id] = []
    # 아래 1줄로 줄일 수 있음
    # user = {id:[] for id in id_list}

    # 유저가 신고한 ID 저장
    for case in report:
        user1, user2 = case.split()
        user[user1].append(user2)

    # 중복 신고 제거
    total_report = []
    for key, val in user.items():
        user[key] = list(set(val))
        total_report += user[key]

    # 정지당한 유저
    ban = []
    for name in user.keys():
        if total_report.count(name) >= k:
            ban.append(name)

    res = []
    for key, val in user.items():
        cnt = 0
        for ban_user in ban:
            if ban_user in val:
                cnt += 1
        res.append(cnt)

    return res


# 다른 풀이
def solution2(id_list, report, k):
    res = [0] * len(id_list)
    dic_report = {id:[] for id in id_list}

    # 중복된 신고는 set()으로 제거하고 {신고당한 유저 : [신고한 유저들]}
    for case in set(report):
        user1, user2 = case.split()
        dic_report[user2].append(user1)

    for key, val in dic_report.items():
        # k번 이상 신고당했으면
        if len(val) >= k:
            # 신고자의 이메일 횟수 +1
            for name in val:
                res[id_list.index(name)] += 1
    
    return res


# test case
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

res = solution2(id_list, report, k)
print('res:', res)
