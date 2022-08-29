using namespace std;

int gcd(int& w, int& h){
    int n;
    while(h != 0){
        n = w % h;
        w = h;
        h = n;
    }
    return w;
}

long long solution(int w,int h) {
    long long answer = 1;
    long long rec_area = (long long)w * h;
    answer = rec_area - (w + h - gcd(w,h));
    return answer;
}
