// 완주하지 못한 선수 (22.06.22)
// https://programmers.co.kr/learn/courses/30/lessons/42576
function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for (let i = 0; i < participant.length; i++){
        if (participant[i] !== completion[i])
            return participant[i]
    }
    return -1;
}