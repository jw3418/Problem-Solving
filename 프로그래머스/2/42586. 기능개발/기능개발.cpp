#include <string>
#include <vector>
#include <deque>
#include <numeric>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    int N = progresses.size();
    
    vector<int> answer;
    int start_idx = 0;
    while (accumulate(answer.begin(), answer.end(), 0) < N)
    {
        for (int i = start_idx; i < N; ++i)
        {
            progresses[i] += speeds[i];
        }
        
        int cnt = 0;
        for (int i = start_idx; i < N; ++i)
        {
            if (progresses[i] >= 100)
            {
                start_idx = i + 1;
                cnt++;
            }
            else
            {
                break;
            }
        }
        
        if (cnt > 0)
        {
            answer.push_back(cnt);
        }
    }

    
    return answer;
}