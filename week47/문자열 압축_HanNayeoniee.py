def solution(s):
    result = []

    # 입력 문자열 길이가 1인 경우
    if len(s) == 1:
        return 1

    # 1부터 문자열 길이까지 쪼개는 단위를 늘려가면서 확인
    for i in range(1, len(s)+1):
        res = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s)+i, i):
            # 이전 subset과 같으면 개수 증가
            if tmp == s[j:j+i]:
                cnt += 1
            # 이전 subset과 다르면 압축한 문자열 만들기
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt)
                    res += tmp
                tmp = s[j:j+i]
                cnt = 1

        result.append(len(res))

    return min(result)