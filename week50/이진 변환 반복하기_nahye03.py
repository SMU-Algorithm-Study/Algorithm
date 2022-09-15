def solution(s):
    cnt=0
    remove_0 = 0
    while s!='1':
        cnt+=1
        remove_0+=s.count('0') #0 개수 세기
        s = s.replace('0','') #0제거
        s = str(format(len(s),'b')) #2진수 변환

    return [cnt,remove_0]

s = "01110"
print(solution(s))

#다른 풀이
# def solution(s):
#     cnt, remove_0 = 0,0
#     while s != '1':
#         cnt+=1
#         num = s.count('1')
#         remove_0 += len(s)-num
#         s = bin(num)[2:]
#     return [cnt, remove_0]