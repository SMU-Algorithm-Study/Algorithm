// [1차]다트 게임 (22.07.12)
// https://school.programmers.co.kr/learn/courses/30/lessons/17682#
function solution(dartResult) {
    let score = [];
    const dartR = dartResult.split('');
    let cnt = 0;
    dartR.forEach((n, idx) =>{
        if (dartR[idx]==='0' && dartR[idx-1]==='1'){
            cnt--;
            score[cnt] = 10;
            cnt++;
        } else if(!isNaN(n)){
            score[cnt] = Number(n);
            cnt++;
        }
        if(n === 'D'){
            score[cnt-1] = Math.pow(score[cnt-1],2);
        }else if(n === 'T'){
            score[cnt-1] = Math.pow(score[cnt-1],3);
        }
        
        if(n === '*'){
            if (cnt>1) score[cnt-2] *= 2;
            score[cnt-1] *= 2;
        }
        if(n === '#'){
            score[cnt-1] *= -1;
        }
    });
        
    return score.reduce((sum, n)=>{return sum+=n},0);
}