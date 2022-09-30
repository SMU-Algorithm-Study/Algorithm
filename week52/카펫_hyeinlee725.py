def solution(brown, yellow):
    carpet = brown + yellow
    for i in range(carpet, 2, -1):
        if carpet  % i == 0: 
            a = carpet // i
            if yellow == (i - 2) * (a - 2):
                    return [i, a]
