// 약수의 개수와 덧셈 (22.07.15)
// https://school.programmers.co.kr/learn/courses/30/lessons/77884
function divisor(n){
let len = 0;
for(let i=1; i<=n; i++){
    if(n%i==0) len++;
}
return len;
}

function solution(left, right) {
let sum = 0;
for(let i=left; i<=right; i++){
    if(divisor(i)%2==0)sum+=i
    else sum-=i
}
return sum;
}