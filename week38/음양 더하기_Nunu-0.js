// 음양 더하기 (22.06.14)
// https://programmers.co.kr/learn/courses/30/lessons/76501
function solution(absolutes, signs) {
    return absolutes.reduce((sum, n, idx)=>sum + n * (signs[idx] ? 1 : -1),0);
}