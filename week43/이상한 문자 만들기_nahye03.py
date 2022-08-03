def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i==' ':
            cnt = 0
            answer += i
        elif cnt%2 == 0:
            answer += i.upper()
            cnt += 1
        else :
            answer += i.lower()
            cnt += 1

    return answer

s = " try hello world haha "
print(solution(s))

#다른 풀이
# def solution(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i%2 else a.upper() for i, a in enumerate(x)]),s.split(" ")))

# " ".join -> 공백을 구분자로 하여 문자열 합치기
# map -> for문처럼