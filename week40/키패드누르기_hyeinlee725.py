def solution(numbers, hand):
    answer = ''
    # 키패드를 좌표료 변경
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    # left, right 각각 시작 위치
    left = keypad['*']
    right = keypad['#']
    for num in numbers:
        if (num in [1, 4, 7]): # left
            answer += 'L'
            left = keypad[num]
        elif (num in [3, 6, 9]): # right
            answer += 'R'
            right = keypad[num]        
        elif (num in [2, 5, 8, 0]): # 좌표 거리 계산(middle)
            left_dis = 0
            right_dis = 0
            for l, r, n in zip(left, right, keypad[num]):
                left_dis += abs(l - n)
                right_dis += abs(r - n)
            if (left_dis < right_dis): # 왼손이 더 가까운 경우
                answer += 'L'
                left = keypad[num]
            elif (left_dis > right_dis): # 오른손이 더 가까운 경우
                answer += 'R'
                right = keypad[num]
            # 왼손, 오른손 거리가 같은 경우
            else:
                if (hand == 'left'): # 왼손잡이
                    answer += 'L'
                    left = keypad[num]
                else: # 오른손잡이
                    answer += 'R'
                    right = keypad[num]
    return 
