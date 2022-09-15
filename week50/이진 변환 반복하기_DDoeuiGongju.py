def solution(s):
    zero_num = 0
    whole_num = 0
    while s != '1':
        whole_num+=1
        cnt_one = 0
        for i in s:
            if i == '0':
                zero_num +=1
            else:
                cnt_one += 1
        s = format(cnt_one,'b')

    answer = [whole_num,zero_num]
    return answer


s = '111100110'
print(solution(s))

