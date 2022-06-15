// 신고 결과 받기 (22.06.08)
// https://programmers.co.kr/learn/courses/30/lessons/92334
function solution(id_list, report, k) {
    var answer = [];
    let reportCnt = {};
    let mailCnt = {};
    let set = Array.from(new Set(report)); // 중복 제거

    id_list.forEach((id) => {
        reportCnt[id] = 0;
        mailCnt[id] = 0;
    })

    set.forEach((reports) => {
        let reportID = reports.split(' ');
        reportCnt[reportID[1]] += 1;
    })

    set.forEach((reports) => {
        let reportID = reports.split(' ');
        if (reportCnt[reportID[1]] >= k) {
            mailCnt[reportID[0]] += 1;
        }
    })

    answer = Object.values(mailCnt);
    return answer;
}