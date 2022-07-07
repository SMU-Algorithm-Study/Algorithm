def solution(x):
    answer = True
    num_sum = 0

    #자리수별로 나누고 더하기
    for i in str(x):
        num_sum += int(i)

    if x % num_sum == 0:
        answer = True
    else:
        answer = False

    return answer

#다른 방법1
# def solution(x):
#     return x % sum([int(i) for i in str(x)])==0

#다른 방법2
# def solution(x):
#     num_sum = sum(map(int, str(x)))
#     return True if x%num_sum==0 else False
