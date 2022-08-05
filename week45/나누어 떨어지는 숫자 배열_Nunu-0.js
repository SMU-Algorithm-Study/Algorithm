// 나누어 떨어지는 숫자 배열 (22.08.06)
// https://school.programmers.co.kr/learn/courses/30/lessons/12910
function solution(arr, divisor) {
    var answer = arr.sort((a,b)=>a-b).filter(n => n%divisor===0);
    return answer.length===0? [-1]:answer;
}