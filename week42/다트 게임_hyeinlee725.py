def solution(dartResult):
    score = ''
    answer = []
    for i in dartResult:
        if i.isnumeric(): # 올바르면
            score += i
        elif i == 'S':
            score = int(score)**1
            answer.append(score)
            score = ''
        elif i == 'D':
            score = int(score)**2
            answer.append(score)
            score = ''
        elif i == 'T':
            score = int(score)**3
            answer.append(score)
            score = ''
        elif i == '*': # 스타상
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2 # 바로 전에 얻은 점수
                answer[-1] = answer[-1] * 2 # 해당 점수
            else: # 첫번째 기회
                answer[-1] = answer[-1] * 2
        elif i == '#': # 아차상('#')
            answer[-1] = answer[-1] * -1 # 해당 점수
    answer = sum(answer)
    return answer
