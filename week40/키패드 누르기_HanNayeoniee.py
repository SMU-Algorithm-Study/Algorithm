# 2022.07.02
# 프로그래머스 - 키패드 누르기(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keypad = {'1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '*': (3, 0),
            '0': (3, 1),
            '#': (3, 2)
            }

    # 두 개의 튜플 간의 거리 구하기
    def get_dist(arr1, arr2):
        return abs(arr1[0] - arr2[0]) + abs(arr1[1] - arr2[1])
        
    # 왼손, 오른손 시작점
    left = '*'
    right = '#'
    
    for num in numbers:
        # 1,4,7은 왼손으로 누름
        if num in [1, 4, 7]:
            answer += 'L'
            left = str(num)

        # 3,6,9는 오른손으로 누름
        elif num in [3, 6, 9]:
            answer += 'R'
            right = str(num)

        # 2,5,8,0은 가까운 손으로 누름
        else:
            # 누르려는 숫자와 양 손간의 거리 구하기          
            left_dist = get_dist(keypad[left], keypad[str(num)])
            right_dist = get_dist(keypad[right], keypad[str(num)])

            # 왼손이 더 가까운 경우
            if left_dist < right_dist:
                answer += 'L'
                left = str(num)  # 왼손 위치 업데이트

            # 오른손이 더 가까운 경우
            elif left_dist > right_dist:
                answer += 'R'
                right = str(num)  # 오른손 위치 업데이트
            
            # 왼손, 오른손 거리가 동일한 경우
            else:
                # 오른손잡이
                if hand == 'right':
                    answer += 'R'
                    right = str(num)  # 오른손 위치 업데이트
                # 왼손잡이
                else:
                    answer += 'L'
                    left = str(num)  # 왼손 위치 업데이트
        
    return answer

# test case
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

answer = solution(numbers, hand)
print('answer:', answer)  # "LRLLLRLLRRL"
