// 조이스틱 (22.09.09)
// https://school.programmers.co.kr/learn/courses/30/lessons/42860
function solution(name) {
    let answer = 0;
    const alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let move = name.length-1;
    
    for(let i=0; i<name.length; i++){
        index = alpabet.indexOf(name[i]);
        answer += index<=13?index : 26-index;
        
        let cnt = i+1;
        while(cnt<name.length&&name[cnt]==='A'){
            cnt++
        }

        move = Math.min(move, (i*2)+name.length-cnt);
        move = Math.min(move, (name.length-cnt)*2+i);
    }

    return answer+move;
}