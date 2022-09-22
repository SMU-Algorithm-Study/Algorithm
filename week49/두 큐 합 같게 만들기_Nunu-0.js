// 두 큐 합 같게 만들기 (22.09.10)
// https://school.programmers.co.kr/learn/courses/30/lessons/118667
function solution(queue1, queue2) {
    const sum = (arr)=>arr.reduce((sum,n)=>sum+n);
    let sum1 = sum(queue1);  
    const aver = (sum1+sum(queue2))/2
    const queue = [...queue1,...queue2];
    let start = 0;
    let end = queue1.length;
    for(let cnt=0; cnt <= queue1.length*2+2; cnt++){
        if(sum1 === aver)
            return cnt;
        if(sum1 < aver)
            sum1+= queue[end++];
        else
            sum1-= queue[start++];
    }
    return -1;
}