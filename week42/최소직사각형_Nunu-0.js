// 최소직사각형 (22.07.13)
// https://school.programmers.co.kr/learn/courses/30/lessons/86491
function solution(sizes) {
    let maxW=0;
    let maxH=0;
    sizes.map(n => n.sort((a,b)=>b-a)).forEach(([w,h])=>{
        maxW = Math.max(w, maxW);
        maxH = Math.max(h, maxH);
    });
    return maxW * maxH;
}