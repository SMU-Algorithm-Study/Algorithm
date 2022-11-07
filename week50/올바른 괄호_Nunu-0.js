// 올바른 괄호 (22.09.17)
// https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=javascript
function solution(s){
    let answer = 0;
    for(let i=0; i<s.length; i++){
        s[i]==='('?answer++:answer--;
        if (answer<0) return false
    }

    return answer===0?true:false;
}