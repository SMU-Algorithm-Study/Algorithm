// 직사각형 별찍기 (22.07.21)
// https://school.programmers.co.kr/learn/courses/30/lessons/12969?language=javascript
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    let rst = ''
    for(let i=0; i<b; i++){
        for(let j=0; j<a; j++){
            rst+='*'
        }
        rst+='\n'
    }
    console.log(rst);
});