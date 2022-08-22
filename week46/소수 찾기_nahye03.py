def is_prime(num):
    if num ==2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime(i):
            answer+=1
    return answer

##다른 풀이(에라토스테네스의 체)
# def solution(n):
#     num = set(range(2, n+1))
#
#     for i in range(2, n+1):
#         if i in num:
#             num-=set(range(2*i, n+1, i))
#     return len(num)