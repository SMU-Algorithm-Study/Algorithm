def solution(n, words):
    answer = [0, 0]
    cnt = 1
    for i in range(1, len(words)):
        w = words[i]
        cnt %= n
        if (words[i] in words[:i]) or (words[i][0] != words[i-1][-1]) :
            answer = [cnt + 1, 1 + i // n]
            return answer
        cnt += 1
    return answer
