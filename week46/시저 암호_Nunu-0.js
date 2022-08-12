// 시저 암호 (22.08.13)
// https://school.programmers.co.kr/learn/courses/30/lessons/12926
function solution(s, n) {
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lower = "abcdefghijklmnopqrstuvwxyz";
    let answer = '';
    for (let i=0; i<s.length; i++){
        if(s[i]===' ') answer += ' ';
        else if(upper.includes(s[i]))
            answer+=upper[(upper.indexOf(s[i])+n)%upper.length];
        else answer+=lower[(lower.indexOf(s[i])+n)%lower.length];
    }
    return answer;
}