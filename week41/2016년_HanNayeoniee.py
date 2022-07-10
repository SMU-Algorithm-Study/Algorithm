# 2022.07.04
# 프로그래머스 - 2016년(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

def solution(a, b):
    # 2016년은 윤년이므로 2월이 29일까지 있음
    month = {1: 31,
            2 : 29,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31
            }
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    # 매월 1일 요일 계산
    start_day = {1 : 'FRI'}
    for i in range(2, 13):
        pre_idx = days.index(start_day[i-1])
        gap = month[i-1] % 7
        next_idx = (pre_idx + gap) % 7
        start_day[i] = days[next_idx]

    # print(start_day)

    # a월 b일 요일 구하기
    start_idx = days.index(start_day[a])
    remain = b % 7
    next_idx = (start_idx + remain) % 7

    return days[next_idx - 1]

# test case
res = solution(5, 24)
print(res)  # 'TUE'
