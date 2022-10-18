def solution(arr):
    answer = 0
    test = 1
    for i in arr:
        answer = test*i
        while(i):
            test, i = i, test%i
        answer /= test
        test = answer
    return answer

print(solution([2,3, 4, 5]))
