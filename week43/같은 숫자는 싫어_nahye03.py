def solution(arr):
    answer = []
    num = 10
    for i in arr:
        if i != num:
            answer.append(i)
            num = i
    return answer

arr =[1,1,3,3,0,1,1]
print(solution(arr))

##다른 방법
# def solution(s):
#     a =[]
#     for i in s:
#         if a[-1:] == [i]: ##a[-1:]은 list
#             continue
#         a.append(i)
#     return a
