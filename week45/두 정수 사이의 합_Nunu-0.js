// 두 정수 사이의 합 (22.08.01)
// https://school.programmers.co.kr/learn/courses/30/lessons/12912
function solution(a, b) {
    let sum = 0;
    const x = Math.min(a,b);
    const y = Math.max(a,b);
    for (let i=x; i<=y; i++)sum+=i;
    return sum;
}