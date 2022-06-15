// 부족한 금액 계산하기 (22.06.15)
// https://programmers.co.kr/learn/courses/30/lessons/82612
function solution(price, money, count) {
    var answer = money;
    for(let i=1; i<=count; i++){
        answer -= price * i;
    }
    return answer > 0? 0 : -answer;
}