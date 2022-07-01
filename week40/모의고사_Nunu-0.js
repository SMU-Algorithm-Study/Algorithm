// 모의고사 (22.07.01)
// https://programmers.co.kr/learn/courses/30/lessons/42840
function marking(answers, P){
    return answers.filter((n, idx)=>n == P[idx%P.length]).length;
}
function solution(answers) {
    let answer = [];
    const P1 = [1, 2, 3, 4, 5];
    const P2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const Score = [marking(answers, P1), marking(answers, P2), marking(answers, P3)];
    const max = Math.max(...Score);
    Score.forEach((n, idx)=>{
        if(max == n)answer.push(idx+1);
    });
    return answer;
}