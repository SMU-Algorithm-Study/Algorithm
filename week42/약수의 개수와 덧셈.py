#약수의 개수 구하는 함수
def get_divisor(n):
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            arr.append(i)
            if i != n//i :
                arr.append(n//i)
    return len(arr)

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_divisor(i) % 2==0:
            answer += i
        else:
            answer -= i

    return answer

#다른 방법
# def solution(left, right):
#     answer = 0
#     for i in range(left, right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer