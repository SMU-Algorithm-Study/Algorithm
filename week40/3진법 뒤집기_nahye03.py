##십진수를 삼진법으로 하고 뒤집은 결과
def change2Ternary(n):
    ternary = []
    while n > 0:
        a = n // 3
        b = n % 3
        ternary.append(b)
        n = a
    return ternary

def solution(n):
    answer = 0

    ter = change2Ternary(n)
    #다시 십진수로
    for i in range(0, len(ter)):
        answer += ter[i] * (3 ** (len(ter) - i - 1))

    return answer

##다른 방법
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n%3)
#         n = n//3
#
#     answer = int(tmp,3)
#     return answer