// 소수 찾기 (22.08.12)
// https://school.programmers.co.kr/learn/courses/30/lessons/12921
function check(n){
    for(let i=2; i<=Math.sqrt(n); i++){
        if(n%i===0)
            return 0;
    }
    return 1;
}
function solution(n) {
    let cnt=0;
    for(let i=2; i<=n; i++){
        cnt += check(i);
    }
    return cnt;
}