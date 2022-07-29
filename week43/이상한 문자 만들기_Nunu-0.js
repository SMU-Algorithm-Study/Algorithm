// 이상한 문자 만들기 (22.07.21)
// https://school.programmers.co.kr/learn/courses/30/lessons/12930
function UpLow(str){
    rst =''
    for(let i=0; i<str.length; i++){
        if (i%2==0){rst += str[i].toUpperCase();}
        else{rst += str[i].toLowerCase();}
    }
    return rst;
}
function solution(s) {
    return s.split(' ').map(str=>UpLow(str)).join(' ');
}