// 제일 작은 수 제거하기 (22.08.10)
// https://school.programmers.co.kr/learn/courses/30/lessons/12935
function solution(a, b) {
    let sum = 0;
    const x = Math.min(a,b);
    const y = Math.max(a,b);
    for (let i=x; i<=y; i++)sum+=i;
    return sum;
}