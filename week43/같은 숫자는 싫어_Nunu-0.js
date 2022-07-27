// 같은 숫자는 싫어 (22.07.22)
// https://school.programmers.co.kr/learn/courses/30/lessons/12906
function solution(arr)
{   
    return arr.filter((n, idx)=> n !== arr[idx+1]);
}