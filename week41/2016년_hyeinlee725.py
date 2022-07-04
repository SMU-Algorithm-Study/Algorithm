def solution(a, b):
    # 1월 1일 : 금요일
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # 각 달의 날짜(2016년 : 윤년 - 2월이 29일까지)
    mon_day = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    # (a-1)월의 날짜를 다 더해서 7로 나눈 나머지 반환
    answer = day[(sum(mon_day[:a - 1]) + b - 1) % 7]
    return answer
