[프로그래머스] 키패드 누르기
def solution(numbers, hand):
    answer = ''
    leftN = [1, 4, 7] # 왼쪽열의 숫자
    rightN = [3, 6, 9] # 오른쪽열의 숫자
    leftH = 10 # 왼손 위치(*)
    rightH = 12 # 오른손 위치(#)
    
    for num in numbers:
        # 왼쪽열의 숫자
        if num in leftN:
            answer += 'L'
            leftH = num
        # 오른쪽열의 숫자
        elif num in rightN:
            answer +='R'
            rightH = num
        else:
            # 숫자가 0일 때 위치 11로 재설정
            if num == 0:
                num = 11
            
            # 숫자와 양 손 간의 간격차 
            leftGap = abs(num - leftH)
            rightGap = abs(num - rightH)
            # 거리
            leftD = leftGap % 3 + leftGap // 3
            rightD = rightGap % 3 + rightGap // 3
            '''
            % = 좌우간의 간격
            // = 상하의 간격
            '''
            # 왼손이 숫자와 더 가깝다면
            if leftD < rightD:
                answer += 'L'
                leftH = num
            # 오른손이 숫자와 더 가깝다면
            elif leftD > rightD:
                answer += 'R'
                rightH = num
            # 양손의 거리가 같다면 
            elif leftD == rightD:
                if hand == 'left':
                    answer += 'L'
                    leftH = num
                else:
                    answer += 'R'
                    rightH = num         
            
    return answer
