import math

def solution(arr):
    num = (arr[0]*arr[1])//math.gcd(arr[0],arr[1])

    for i in range(2, len(arr)):
        num = (num*arr[i])//math.gcd(num, arr[i])

    return num

arr = [2,6,8,14]
print(solution(arr))
