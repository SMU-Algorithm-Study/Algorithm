// 멀쩡한 사각형(22.09.09)
// https://school.programmers.co.kr/learn/courses/30/lessons/62048?language=javascript
function gcd(a,b){
    const n = a%b;
    if (n === 0)
        return b;
    return gcd(b, n);
}

function solution(w, h) {
    return (w*h)-(w+h-gcd(w,h));
}