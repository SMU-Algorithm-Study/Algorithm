// 가운데 글자 가져오기 (22.07.27)
// https://school.programmers.co.kr/learn/courses/30/lessons/12903
function solution(s) {
    let answer = '';
    const len = s.length;
    if(len%2 === 0) answer = s[len/2-1] + s[len/2]
    else answer = s[Math.floor(len/2)]
    return answer;
}