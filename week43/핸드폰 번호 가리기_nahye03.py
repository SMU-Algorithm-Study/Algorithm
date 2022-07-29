def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer += '*'
    answer = answer + phone_number[-4:]
    return answer

phone_number="01033334444"
print(solution(phone_number))

#다른 방법
# def solution(phone_number):
#     return '*'*(len(phone_number)-4)+phone_number[-4:]