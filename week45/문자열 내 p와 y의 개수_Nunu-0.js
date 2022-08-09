// 문자열 내 p와 y의 개수 (22.08.06)
// https://school.programmers.co.kr/learn/courses/30/lessons/12916
function solution(s){
    cntP = s.toUpperCase().split("P").length
    cntY = s.toUpperCase().split("Y").length;
    return cntP===cntY? true: false;
}