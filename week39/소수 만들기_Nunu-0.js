// 소수 만들기 (22.06.21)
// https://programmers.co.kr/learn/courses/30/lessons/12977
function prime(num){
    for (let i = 2; i <= Math.sqrt(num); i++){
        if(num % i === 0){
            return false;
        }
    }
    return true;
}

function solution(nums) {
    let answer = 0;
    
    for (let i = 0; i < nums.length; i++){
        for(let j = i+1; j < nums.length; j++){
            for(let k = j+1; k < nums.length; k++){
                const num = nums[i] + nums[j] + nums[k];
                prime(num)? answer++ : answer;
            }
        }
    }
    
    return answer;
}