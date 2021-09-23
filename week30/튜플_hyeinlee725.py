def solution(s):
    answer = []
    # [2:-2]로 맨앞'{{'와 맨뒤'}}'를 자르고, '}.{'를 기준으로 split
    s_list = s[2:-2].split('},{') # 괄호문자가 모두 사라짐
    # 원소의 길이를 기준으로 정렬
    s_list.sort(key = len)
    for num in s_list:
        # ',' 기준으로 split
        num = num.split(',')
        for n in num:
            # n이 answer에 없으면
            if (int(n) not in answer):
                # answer 배열에 append
                answer.append(int(n))
    return answer
