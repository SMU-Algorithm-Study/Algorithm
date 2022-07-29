// 핸드폰 번호 가리기 (22.07.20)
// https://school.programmers.co.kr/learn/courses/30/lessons/12948
function solution(phone_number) {
    const answer = '*'.repeat(phone_number.length-4)+phone_number.slice(-4);
    return answer;
}