# 정답 코드 출처: https://whatryando.tistory.com/142

def solution(name):
    answer = 0
    # A -> 각 알파벳으로 만드는 횟수 세기 (상하 방향)
    for n in name:
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
    min_move = len(name) - 1
    
    # 좌우 방향 횟수 세기
    for i in range(len(name)):    
        next_i = i+1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1

        # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    
    return answer + min_move