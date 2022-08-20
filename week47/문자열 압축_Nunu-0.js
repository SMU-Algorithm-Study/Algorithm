// 문자열 압축 (22.08.17)
// https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=javascript
function solution(s) {
  var answer = [];
  for (let i=1; i<s.length/2+1;i++){
      let str = '';
      let cnt = 1;
      let word = s.slice(0,i);
      for (let j=0; j<=s.length;j+=i){
          let nextWord=s.substr(j+i,i);
          if(nextWord===word){
              cnt+=1;
          }else{
              cnt>1? str+=cnt+word:str+=word;
              word = nextWord;
              cnt = 1;
          }
      }
      answer.push(str.length);
  }
  return Math.min(...answer);
}