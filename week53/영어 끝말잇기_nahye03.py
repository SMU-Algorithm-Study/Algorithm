def solution(n, words):
    answer =[]
    w = [words[0]]
    for i in range(1, len(words)):
        if (words[i] in w) or (w[i-1][-1]!=words[i][0]):
            answer=[i%n+1, i//n+1]
            break
        w.append(words[i])
    if not answer:
        answer=[0,0]

    return answer

n=2
words =["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))

#다른 풀이
# for i in range(1, len(words)):
#     if words[i][0]!=words[i-1][-1] or words[i] in words[:i]:
#         return [(i%n)+1, (i//n)+1]
# else:
#     return [0,0]
