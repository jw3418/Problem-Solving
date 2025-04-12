#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {    
    deque<pair<int ,int>> dq;   // {우선순위, 인덱스}
    
    for (int i = 0; i < priorities.size(); ++i)
    {
        dq.push_back({priorities[i], i});
    }
    
    int order = 1;
    while (!dq.empty())
    {
        pair<int, int> cur_pair = dq.front();
        dq.pop_front();
        
        bool flag = true;
        for (int i = 0; i < dq.size(); ++i)
        {
            if (cur_pair.first < dq[i].first)
            {
                dq.push_back(cur_pair);
                flag = false;
                break;
            }
        }
        if (flag)
        {
            if (cur_pair.second == location)
            {
                return order;
            }
            order++;
        }
    }
    
}