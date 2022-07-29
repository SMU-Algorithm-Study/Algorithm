// 두 개 뽑아서 더하기 (22.07.15)
// https://school.programmers.co.kr/learn/courses/30/lessons/68644
function solution(numbers) {
    const set = new Set();
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            set.add(numbers[i] + numbers[j])
        }
    }
    const answer = [...set]
    return answer.sort((a, b) => a - b)
}