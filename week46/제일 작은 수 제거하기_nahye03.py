def solution(arr):
    answer = []
    if(len(arr)==1):
        answer.append(-1)
    else:
        min_num = min(arr)
        for i in arr:
            if i!=min_num:
                answer.append(i)
        #[i for i in arr if i>min(arr)]
    return answer