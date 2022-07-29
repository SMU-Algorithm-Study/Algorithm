def solution(n, arr1, arr2):
    answer = []
    arr_bin =[]

    #비트 연산자 사용
    for i in range(n):
        arr_bin.append(bin(arr1[i]|arr2[i])[2:].zfill(n))

    for i in arr_bin:
        answer.append(i.replace('1','#').replace('0',' '))

    return answer

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
