// 예산 (22.07.01)
// https://programmers.co.kr/learn/courses/30/lessons/12982
function solution(d, budget) {
    return d.sort((a,b)=>a-b).reduce((cnt, n)=>{
        budget -= n;
        if(budget >= 0)cnt++;
        return cnt
    },0);
}