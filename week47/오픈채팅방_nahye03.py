def solution(record):
    answer = []

    #최종 아이디와 닉네인
    id_name = {}
    for i in record:
        tmp = i.split()
        if tmp[0]!='Leave':
            id_name[tmp[1]] = tmp[2]

## printer = {'Enter':'님이 들어~', 'Leave':'님이 나갔~'}
    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter':
            answer.append(id_name[tmp[1]]+'님이 들어왔습니다.') #printer[tmp[0]]
        elif tmp[0] == 'Leave':
            answer.append(id_name[tmp[1]]+'님이 나갔습니다.')
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
