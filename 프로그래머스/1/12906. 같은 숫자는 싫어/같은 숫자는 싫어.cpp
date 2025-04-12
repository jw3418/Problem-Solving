#include <vector>
#include <deque>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    deque<int> dq;
    for (int i = 0; i < arr.size(); ++i)
    {
        if (!dq.empty())
        {
            if (dq.back() == arr[i])
            {
                continue;
            }
            else
            {
                dq.push_back(arr[i]);
            }
        }
        else
        {
            dq.push_back(arr[i]);
        }
    }
    
    vector<int> answer;
    while (!dq.empty())
    {
        answer.push_back(dq.front());
        dq.pop_front();
    }

    return answer;
}