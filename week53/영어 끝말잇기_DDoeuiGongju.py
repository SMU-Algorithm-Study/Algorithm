def solution(n, words):
    wordset = [words[0]]
    number, order = 0, 1
    for i in range(1, len(words)):
        if i % n == 0:
            order += 1
        if words[i] not in wordset:
            wordset.extend([words[i]])
        else:
            number = i % n + 1
            break
        if words[i-1][-1] != words[i][0]:
            number = i % n + 1
            break
    if words == wordset:
        number, order = 0, 0
    return number, order


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))