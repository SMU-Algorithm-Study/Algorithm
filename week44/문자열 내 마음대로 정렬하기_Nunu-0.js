// 문자열 내 마음대로 정렬하기 (22.07.31)
// https://school.programmers.co.kr/learn/courses/30/lessons/12915
function solution(strings, n) {
  return strings.sort((a, b)=>a[n]>b[n] ? 1 : a[n]<b[n]? -1: a>b? 1 : -1);
}