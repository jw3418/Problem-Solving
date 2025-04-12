#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    
    priority_queue<int> pq;
    for (int i = 0; i < scoville.size(); ++i)
    {
        pq.push(-scoville[i]);
    }
    
    int cnt = 0;
    while ((pq.size() >= 2) && (-pq.top() < K))
    {
        int one = -pq.top(); pq.pop();
        int two = -pq.top(); pq.pop();
        pq.push(-(one + 2 * two));
        
        cnt++;
    }
    
    if (-pq.top() < K)
    {
        return -1;
    }
    return cnt;
}