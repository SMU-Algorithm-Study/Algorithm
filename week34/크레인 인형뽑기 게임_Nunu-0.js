function solution(board, moves) {
    let answer = 0;
    const basket = []; // const == static

    // forEach(): moves의 각각의 요소를 move에 넣음
    // python의 `for move in moves`이라 생각하면 된다
    moves.forEach((move)=>{
        for (let i = 0; i < board.length; i++){
            const doll = board[i][move-1];
            //doll이 0이 아니라면
            if(doll){
                // 같은 인형이 앞에 있는지 확인
                if(basket[basket.length-1] === doll){
                    answer+= 2;
                    basket.pop();
                }
                else basket.push(doll);

                board[i][move-1] = 0; //뽑은 위치 비움으로 초기화
                break;
            }
        }
    });

    return answer;
}
