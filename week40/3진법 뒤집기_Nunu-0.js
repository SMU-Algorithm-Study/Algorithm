// 3진법 뒤집기 (22.07.01)
// https://programmers.co.kr/learn/courses/30/lessons/68935
function solution(n) {
    const change = n.toString(3).split('').reverse().join('');
    return parseInt(change, 3);
}