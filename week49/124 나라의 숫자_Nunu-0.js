// 124 나라의 숫자 (22.09.10)
// https://school.programmers.co.kr/learn/courses/30/lessons/12899#
function solution(n) {
    const rule='412';
    let num='';
    while(n){
        num=rule[n%3]+num;
        n = (n%3===0)?n/3-1:Math.floor(n/3);
    }
    return num;
}