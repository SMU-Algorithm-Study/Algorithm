// 오픈채팅방 (22.08.17)
// https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=javascript
function solution(record) {
  let act = [];
  const users = {};
  record.forEach((n)=>{
      const user = n.split(' ');
      if(user[0]==='Leave') {
          act.push([user[1], '님이 나갔습니다.']);
          return;
      }
      else if(user[0]==='Enter') act.push([user[1], '님이 들어왔습니다.']);
      users[user[1]]=user[2];
  })
  return act.map((n)=>users[n[0]]+n[1]);
}