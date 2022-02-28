using namespace std;

int gcd(int& w, int& h) { //w와 h의 최대공약수
    int n;
    while (h != 0) {
        n = w % h;
        w = h;
        h = n;
    }
    return w;
}

long long solution(int w, int h) {
    long long answer = 1;
    long long rec_area = (long long)w * h;//직사각형 넓이
    answer = rec_area - (w + h - gcd(w, h));//사용할 수 있는 정사각형 개수
    return answer;
}