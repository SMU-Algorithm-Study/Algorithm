def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        tmp = bin(a1 | a2) # 2진수로 변환
        tmp = tmp[2:].zfill(n) # 앞을 0으로
        tmp = tmp.replace('1','#') # 1이면 #
        tmp = tmp.replace('0',' ') # 0이면 공백
        answer.append(tmp)
    return answer
