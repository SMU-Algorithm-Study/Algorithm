// 최솟값 만들기 (22.09.16)
// https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=javascript
function solution(A,B){
    A.sort((a,b)=>a-b)
    B.sort((a,b)=>b-a)
    return A.reduce((sum, a, idx)=>sum+=a*B[idx],0);
}