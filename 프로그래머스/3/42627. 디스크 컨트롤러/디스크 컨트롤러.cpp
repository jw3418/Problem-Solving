#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int N = jobs.size();
    int Sum = 0;
    
    priority_queue<vector<int>> pq; //{소요시간, 요청시각}
    int j_cnt = 0; int cur_sec = 0; int pre_sec = -1;
    while (j_cnt < N)
    {
        for (auto &job : jobs)
        {
            if ((job[0] > pre_sec) && job[0] <= cur_sec)
            {
                pq.push({-job[1], -job[0]});
            }
        }
        if (!pq.empty())
        {
            vector<int> tjob = pq.top();
            pq.pop();
            pre_sec = cur_sec;
            cur_sec += (-tjob[0]);
            Sum += (cur_sec - (-tjob[1]));
            j_cnt++;
        }
        else
        {
            cur_sec++;
        }
    }
    
    return int(Sum / N);
}