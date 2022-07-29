import re
def solution(dartResult):
    answer = 0
    arr = []

    m = re.findall('([0-9]+)([SDT])([*#]?)', dartResult) #규칙에 맞는 값들 다 찾아내기, ()사용해서 구분해주기!

    for i in m:
        if i[1] == "S":
            arr.append(int(i[0]))
        elif i[1] == "D":
            arr.append(int(i[0]) ** 2)
        elif i[1] == "T":
            arr.append(int(i[0]) ** 3)

        if len(i) > 2:
            if i[2] == "*":
                if len(arr) > 1:
                    arr[-1] = arr[-1] * 2
                    arr[-2] = arr[-2] * 2
                else:
                    arr[-1] = arr[-1] * 2
            elif i[2] == "#":
                arr[-1] = arr[-1] * (-1)

        answer = sum(arr)
    return answer

dartResult = "1D2S#10S"
print(solution(dartResult))


#다른 풀이
# def solution(dartResult):
#     bonus = {'S':1, 'D':2,'T':3}
#     option = {'':1, '*':2, '#':-1}
#     p = re.compile('(\d+)([SDT])([*#?])')
#     dart = p.findall(dartResult)
#
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i>0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
#
#     answer = sum(dart)
#     return answer

