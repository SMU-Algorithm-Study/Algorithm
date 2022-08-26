def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next_alp = i + 1
        while next_alp < len(name) and name[next_alp] == 'A':
            next_alp += 1
        min_move = min([min_move, 2 *i + len(name) - next_alp, i + 2 * (len(name) -next_alp)])
    answer += min_move
    return answer
