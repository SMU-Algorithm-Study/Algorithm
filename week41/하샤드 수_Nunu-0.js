// 하샤드 수 (22.07.06)
// https://school.programmers.co.kr/learn/courses/30/lessons/12947
function solution(x) {
    const xStr = [...String(x)];
    const sum = xStr.reduce((s, n)=>s+=Number(n),0);
    return x%sum? false:true;
}