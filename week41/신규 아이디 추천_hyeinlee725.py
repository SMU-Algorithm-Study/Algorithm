def solution(new_id):
    answer = ''
    # 1단계 : 소문자 치환
    new_id = new_id.lower()
    # 2단계 : 문자 제거
    for id in new_id:
        if id.isalnum() or id in '-_.':
            answer += id
    # 3단계 : . 압축
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계 : 양끝 . 제거
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5단계 : 빈 문자열 - a 추가
    if answer == '':
        answer = 'a'
    # 6단계 : 처음 15문자 제외하고 모두 제
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 2자 이하면 마지막 문자 추가
    while len(answer) < 3:
        answer += answer[-1]
    return answer
