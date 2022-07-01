// K번째수 (22.07.01)
// https://programmers.co.kr/learn/courses/30/lessons/42748
function solution(array, commands) {
    let answer = [];
    commands.forEach(arr=>{
        const newArray = array.slice(arr[0]-1, arr[1]);
        newArray.sort((a,b)=>a-b);
        answer.push(newArray[arr[2]-1]);
    });
    return answer;
}