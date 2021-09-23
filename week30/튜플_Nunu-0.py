[프로그래머스] 튜플
def solution(s):
    result = []
    
    # 괄호를 공백으로 바꿔 split로 문자를 나눔
    tuple = s.replace('{{',' ').replace('}}',' ').replace('},{', ' ').split() 
    
    tuple.sort(key = len) # tuple안 집합을 길이 순서대로 정렬
    
    for set in tuple:
        elemt = set.split(',') # ,를 기준으로 리스트로 나누기
        for num in elemt:
            if int(num) not in result: # 포함돼 있지 않은 숫자를 결과에 추가
                result.append(int(num))

    return result
