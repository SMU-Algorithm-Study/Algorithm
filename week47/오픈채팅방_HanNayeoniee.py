from collections import defaultdict

def solution(record):

    users = defaultdict(str)
    result = []

    # 최종 닉네임 받아오기
    for log in record:
        if len(log.split()) == 3:
            status, uid, name = log.split()
            users[uid] = name  # Enter, Change인 경우에만 사용자 이름 update

    # 채팅방 로드 출력
    for log in record:
        if len(log.split()) == 2:
            status, uid = log.split()
            # print("status: {}, uid:{}".format(status, uid))
        else:
            status, uid, name = log.split()
            # print("status: {}, uid:{}, name:{}".format(status, uid, name))

        if status == "Enter":
            result.append(users[uid] + "님이 들어왔습니다.")
        elif status == "Leave":
            result.append(users[uid] + "님이 나갔습니다.")

    return result

# solution()과 비슷하지만 Enter, Leave만 따로 order에 저장함
# 첫번째는 for문을 더 돌지만, 정보를 저장할 추가적인 리스트가 필요하지 않음
def solution2(record):
    answer = []
    order = []  # (uid, 행동)
    
    names = {}  # {uid:이름} 저장
    for message in record:
        mes = message.split()
        if len(mes) == 3:
            names[mes[1]] = mes[2]
        if mes[0] != 'Change':
            order.append((mes[1], mes[0]))
        
    for ord in order:
        if ord[1] == "Enter":
            answer.append(names[ord[0]]+"님이 들어왔습니다.")
        else:
            answer.append(names[ord[0]]+"님이 나갔습니다.")
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
res = solution(record)