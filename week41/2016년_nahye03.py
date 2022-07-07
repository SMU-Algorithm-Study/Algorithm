def solution(a, b):
    answer = ''
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] #요일
    month_cnt = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #달의 일 수

    if a == 1:
        answer = days[(b - 2) % 7 - 1] #일주일로 나눈 후 나머지로 요일 추측
    else:
        sum = 0
        for i in range(a - 1):
            sum += month_cnt[i]
        answer = days[(sum + b - 2) % 7 - 1]

    return answer

#다른 방법
# def solution(a, b):
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']  # 요일을 금요일부터
#     month_cnt = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 달의 일 수
#
#     return days[(sum(month_cnt[:a-1])+b-1)%7]