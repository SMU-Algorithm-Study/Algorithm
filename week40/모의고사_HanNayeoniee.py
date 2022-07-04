# 2022.06.29
# 프로그래머스 - 모의고사(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    
    # 정답과 찍기 규칙으로 맞춘 문제 개수 구하기
    def get_score(answers, p):

        # 찍기 규칙을 조작해 정답 길이와 동일하게 만들기
        mok = len(answers) // len(p)
        remain = len(answers) % len(p)
        my_answers = p * mok + p[:remain]

        # 정답과 찍은게 같으면 +1
        score = sum([1 if answers[i] == my_answers[i] else 0 for i in range(len(answers))])

        return score
    
    # 3명의 찍기 규칙
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s1 = get_score(answers, p1) 
    s2 = get_score(answers, p2)
    s3 = get_score(answers, p3)

    # {사람 번호: 점수}로 저장
    answer = {'1': s1,
             '2': s2,
             '3': s3}
    
    # 많이 맞춘 사람 순서로 정렬
    scores = sorted(answer.items(), reverse=True, key=lambda x:x[1])
    res = [int(p[0]) for p in scores]  # 사람 번호만 저장
    values = [score[1] for score in scores]  # 점수만 저장
    max_num = values.count(values[0])  # 최대 점수를 가진 사람이 몇 명인지
    
    # 최대 점수를 가지는 사람 명수대로 반환
    return res[:max_num]



### main
# answers = [1, 2, 3, 4, 5]
answers = [1, 3, 2, 4, 2]

res = solution(answers)
print('res:', res)