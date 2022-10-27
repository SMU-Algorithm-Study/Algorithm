import math

def solution(fees, records):
    dic = {}
    for record in records:
        time, num, status = record.split()
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])

        if num not in dic:
            dic[num] = [0, time, status]
        if status == 'IN':
            dic[num] = [dic[num][0], time, status]
        else: ##out
            total_t, t, _ = dic[num]
            total_t += time-t
            dic[num] = [total_t, time, status]

    answer = {}
    for num in dic.keys():
        total_t, t, status = dic[num]
        if status == 'IN':
            total_t += 1439-t
        fee = fees[1]
        if total_t>fees[0]:
            fee += math.ceil((total_t-fees[0])/fees[2])*fees[3]
        answer[num] = fee

    return list(map(lambda x:x[1], sorted(answer.items())))


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))