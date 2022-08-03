def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return sorted(answer)

##다른 풀이
# sorted([n for n in arr if n%divisor==0]) or [-1]