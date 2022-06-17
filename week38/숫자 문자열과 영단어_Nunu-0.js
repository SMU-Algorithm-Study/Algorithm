// 숫자 문자열과 영단어 (22.06.16)
// https://programmers.co.kr/learn/courses/30/lessons/81301
function solution(s) {
    let answer = s;
    numS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    numS.forEach((num, idx)=>{
        arr = answer.split(num);
        answer = arr.join(idx);
    });
    return Number(answer);
}