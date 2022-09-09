// 가장 큰 수 (22.08.23)
// https://school.programmers.co.kr/learn/courses/30/lessons/42746
function solution(numbers) {
    const set = [];
    function makeNum(num, arr){
        if(arr.length===0){
            set.push(parseInt(num));
            return
        }
        for (let i=0;i<arr.length;i++){
            let newNum=num+arr[i];
            let newArr=[...arr];
            newArr.splice(i,1);
            makeNum(newNum, newArr);   
        }
    }
    makeNum('',numbers);

    return String(Math.max(...set));
}