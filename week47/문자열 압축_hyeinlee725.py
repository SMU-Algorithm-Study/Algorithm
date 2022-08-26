def solution(s):
    length = []
    if len(s) == 1:
        return 1
    for cut in range(1, (len(s) // 2) + 1):
        answer = ""
        cnt = 1
        ini_st = s[:cut]
        for i in range(cut, len(s), cut):
            if (ini_st == s[i:cut + i]):
                cnt += 1
            else:
                if (cnt == 1):
                    answer += ini_st
                else:
                    answer += str(cnt) + ini_st
                ini_st = s[i:i + cut]
                cnt = 1
        if (cnt == 1):
            answer += ini_st
        else:
            answer += str(cnt) + ini_st
        length.append(len(answer))
    return min(length)
