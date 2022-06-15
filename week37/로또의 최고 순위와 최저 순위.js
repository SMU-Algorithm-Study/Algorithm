// 로또의 최고 순위와 최저 순위 (21.06.09)
// https://programmers.co.kr/learn/courses/30/lessons/77484
function solution(lottos, win_nums) {
    const answer = [];
    const min = lottos.filter(num=>win_nums.includes(num)).length;
    const max = lottos.filter(num=>num===0).length+min;
    
    max > 1 ? answer.push(7-max) : answer.push(6);
    min > 1 ? answer.push(7-min) : answer.push(6);

    return answer;
}