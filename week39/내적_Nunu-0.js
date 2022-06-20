// 내적 (22.06.20)
// https://programmers.co.kr/learn/courses/30/lessons/70128
function solution(a, b) {
  const answer = a.reduce((sum, n, idx)=>{
      return sum += n * b[idx];
  }, 0);
  return answer;
}