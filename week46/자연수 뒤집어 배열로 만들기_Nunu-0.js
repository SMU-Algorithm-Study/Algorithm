// 자연수 뒤집어 배열로 만들기 (22.08.12)
// https://school.programmers.co.kr/learn/courses/30/lessons/12932
function solution(n) {
    return n.toString().split('').reverse().map(n=>Number(n));
}