// 키패드 누르기 (22.07.01)
// https://programmers.co.kr/learn/courses/30/lessons/67256?language=javascript
function solution(numbers, hand) {
    let answer = '';
    const Lnum = [1, 4, 7];
    const Rnum = [3, 6, 9];
    const Cnum = [2,5,8,11];
    let Lpos = 10; // 왼손 위치(*)
    let Rpos = 12; // 오른손 위치(#)
    
    numbers.forEach(n =>{
        if (Lnum.includes(n)){
            answer += 'L';
            Lpos = n;
        }
        else if(Rnum.includes(n)){
            answer += 'R';
            Rpos = n;
        }
        else{
            if (n == 0) n = 11;
            
            const Ldis = Cnum.includes(Lpos)?Math.abs(n - Lpos)/3:Math.abs(n-Lpos-1)/3+1;
            const Rdis = Cnum.includes(Rpos)?Math.abs(n - Rpos)/3:Math.abs(n-Rpos+1)/3+1;   
            console.log(Ldis, Rdis)
            if (Ldis < Rdis){
                answer += 'L';
                Lpos = n;
            }
            else if (Ldis > Rdis) {
                answer += 'R';
                Rpos = n;
            }
            else{
                if (hand == 'left'){
                    answer += 'L';
                    Lpos = n;
                }
                else{
                    answer += 'R';
                    Rpos = n;
                }
            }
        }
    });
    return answer
}