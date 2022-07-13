// 2016년 (22.07.06)
// https://school.programmers.co.kr/learn/courses/30/lessons/12901
function solution(a, b) {
    const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const dates = [31,29,31,30,31,30,31,31,30,31,30,31];
    
    let date = 0;
    for(let i=0; i<a-1; i++) date += dates[i];
    date = (date + b + 4) % 7;
    
    return days[date];
}