#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> basket;//인형을 뽑아서 보관할 바구니(stack)
    for (int i = 0; i < moves.size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            if (board[j][moves[i] - 1] != 0) {//board에 인형이 있으면 뽑기
                if (!basket.empty()) {//stack에 인형이 없으면 같은지 확인 X
                    //stack이 비어있지 않으면, 최상단에 같은 인형이 있는지 확인
                    if (basket.top() == board[j][moves[i] - 1]) {//같은 경우
                        answer += 2;//2개씩 터지므로 +2
                        basket.pop();//터진 인형 pop
                    }
                    else {//다른 경우
                        basket.push(board[j][moves[i] - 1]);
                    }
                }
                else {
                    basket.push(board[j][moves[i] - 1]);
                }
                board[j][moves[i] - 1] = 0;//board에서 뽑음
                break;
            }
        }
    }
    return answer;
}