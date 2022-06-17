// 신규 아이디 추천 (22.06.17)
// https://programmers.co.kr/learn/courses/30/lessons/72410
function solution(new_id) {
  let answer = new_id
      .toLowerCase() //1 
      .replace(/[^\w-_.]/g,'')
      .replace(/\.{2,}/g,'.')
      .replace(/^\.|\.$/g,'')
      .substring(0,15)
      .replace(/^\.|\.$/g,'');
  if(answer==='') answer = 'a';
  while(answer.length < 3) answer += answer.substr(-1);

  return answer;
}