// 실패율 (22.06.25)
// https://programmers.co.kr/learn/courses/30/lessons/42889
function solution(N, stages) {
    const stage = [];
    
    for(let i = 1; i <= N; i++){
        const succ = stages.filter(x => x >= i).length;
        const chall = stages.filter(x => x === i).length;
        stage.push([i, chall/succ]);
    }

    stage.sort((a,b) => b[1] - a[1])
    return stage.map(x => x[0]);
}