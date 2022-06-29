def solution(numbers, hand):
    answer = ''
    left_pos = [3,0] #왼손 위치
    right_pos = [3,2] #오른손 위치
    for i in numbers:
        #무조건 왼손 사용하는 경우
        if i==1 or i==4 or i==7 :
            answer += "L"
            left_pos = [i//3,0]
        #무조건 오른손 사용하는 경우
        elif i==3 or i==6 or i==9 :
            answer += "R"
            right_pos = [i//3-1, 0]
        #가운데 숫자의 경우
        else:
            # 숫자가 있는 위치
            if i == 0:
                num_pos = [3,1]
            else:
                num_pos = [i//3,1]
            left_dist = abs(num_pos[0]-left_pos[0])+abs(num_pos[1]-left_pos[1]) #왼손에서부터 거리
            right_dist = abs(num_pos[0] - right_pos[0]) + abs(num_pos[1] - right_pos[1]) #오른손에서부터 거리
            #거리가 같은 경우
            if left_dist == right_dist:
                if hand == "right":
                    answer += "R"
                    right_pos = num_pos
                else:
                    answer += "L"
                    left_pos = num_pos
            #왼손이 더 가까운 경우
            elif left_dist < right_dist:
                answer += "L"
                left_pos = num_pos
            #오른손이 더 가까운 경우
            else:
                answer += "R"
                right_pos = num_pos

    return answer
#
# numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
#
# print(solution(numbers, hand))

## 다른 풀이
def solution(numbers, hand):
    anwser = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'

    for i in numbers:
        if i in left:
            anwser += "L"
            lhand = i
        elif i in right:
            anwser += "R"
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0])+abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0])+abs(curPos[1]-rPos[1])

            if ldist<rdist:
                anwser += "L"
                lhand = i
            elif ldist >rdist:
                anwser += "R"
                rhand = i
            else:
                if hand == "left":
                    anwser += "L"
                    lhand = i
                else:
                    anwser += "R"
                    rhand = i

    return anwser