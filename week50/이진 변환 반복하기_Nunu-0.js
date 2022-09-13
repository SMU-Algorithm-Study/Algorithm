// 이진 변환 반복하기 (22.09.13)
// https://school.programmers.co.kr/learn/courses/30/lessons/70129
function solution(s) {
  let answer = [0, 0];
  let currS = s
  while(currS>1){
      answer[0]++;
      answer[1] += currS.length-currS.replace(/0/g,'').length;
      currS = currS.replace(/0/g,'').length.toString(2);
  }
  return answer;
}