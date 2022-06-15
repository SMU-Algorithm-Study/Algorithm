// 없는 숫자 더하기 (22.06.14)
// https://programmers.co.kr/learn/courses/30/lessons/86051
function solution(numbers) {
    let answer = -1;
    num = [...Array(10)].map((n, i)=>i);
    
    answer = num.reduce((sum, n)=>{
        sum += !numbers.includes(n) && n;
        return sum;
    },0);
    return answer;
}