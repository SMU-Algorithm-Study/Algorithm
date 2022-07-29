// [1차]비밀지도 (22.07.13)
//https://school.programmers.co.kr/learn/courses/30/lessons/17681
function change2(a, b, len){
    const to2 = (a|b).toString(2);
    return to2.length==len?to2:'0'.repeat(len-to2.length)+to2;
}
function solution(len, arr1, arr2) {
    return arr1.map((num, idx)=>change2(num, arr2[idx], len).replace(/0/g, ' ').replace(/1/g, '#'));
}