def solution(s):
    min_cnt = 10000
    if len(s)==1:
        min_cnt = 1
    else:
        for i in range(1, len(s)//2+1):
            answer = ''
            tmp = s[:i]
            cnt = 1
            print(tmp)
            for j in range(i, len(s)+i, i):
                if tmp==s[j:j+i]:
                    cnt+=1
                    print('akwek')
                else:
                    if cnt==1:
                        answer+=tmp
                        print('이경우')
                    else:
                        answer+=str(cnt)+tmp
                    tmp = s[j:j + i]
                    cnt=1
            min_cnt = min(min_cnt, len(answer))
    return min_cnt

s='a'
print(solution(s))