// 폰켓몬 (22.07.08)
// https://school.programmers.co.kr/learn/courses/30/lessons/1845
function solution(nums) {
    const setLen = new Set(nums).size;
    return setLen<=nums.length/2?setLen:nums.length/2;
}