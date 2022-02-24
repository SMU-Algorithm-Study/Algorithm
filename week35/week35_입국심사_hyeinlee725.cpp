#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end()); //최대 시간 알기 위해 정렬
    long long minTime = 1; //최소 시간
    long long maxTime = (long long) times[times.size() - 1] * n; //최대 시간
    long long mid;

    while (minTime <= maxTime) {
        mid = (minTime + maxTime) / 2; //중앙값
        long long count = 0; //mid 시간동안 심사할 수 있는 사람 수
        for (int i = 0; i < times.size(); i++) {
            count += mid / times[i]; //+각 시간별 처리할 수 있는 사람 수
        }
        if (count < n) {
            minTime = mid + 1; //최소값을 mid + 1로
        }
        else { //mid 시간 동안 처리할 수 있는 사람들이 n명 이상
            if (mid <= maxTime) { // mid가 최대시간이하이면
                answer = mid;
            }
            maxTime = mid - 1; //범위 줄이기(최대값을 mid - 1)
        }
    }
    return answer;
}