// x만큼 간격이 있는 n개의 숫자 (22.07.27)
// https://school.programmers.co.kr/learn/courses/30/lessons/12954
function solution(x, n) {
    return Array.from({length: n}, (undefined, i) => x*(i+1));
}