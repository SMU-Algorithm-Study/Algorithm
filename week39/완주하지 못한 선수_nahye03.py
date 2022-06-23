def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        if i==len(completion):
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# print(solution(participant, completion))

##다른 방법 1
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant)-collections.Counter(completion)
#     return list(answer.keys())[0]


##다른 방법 2
# def solution(participant, completion):
#     answer =''
#     temp = 0
#     dic ={}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer

##다른 방법 3
# def solution(participant, completion):
#     d = {}
#     for p in participant:
#         d[p] = d.get(p)+1
#     for c in completion:
#         d[c] -= 1
#
#     dnf = [k for k,v in d.items() if v>0]
#     answer = dnf[0]
#     return answer