def solution(seoul):
    answer = str(seoul.index('Kim'))

    return '김서방은 '+answer+'에 있다'

seoul = ["Jane", "Kim"]
print(solution(seoul))

#다른 방법
# def solution(seoul):
#     return "김서방은 {}에 있다".format(seoul.index("Kim"))