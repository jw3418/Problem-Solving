#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    
    sort(citations.begin(), citations.end(), [](const int &a, const int &b)
         {
             return a > b;
         });
    
    // for (auto &it: citations)
    // {
    //     cout << it << " ";
    // }
    
    int H_idx = citations[0];
    while (H_idx >= 0)
    {
        int larger_cnt = 0;
        for (auto &it : citations)
        {
            if (H_idx <= it)
            {
                larger_cnt++;
            }
        }
        if (larger_cnt >= H_idx)
        {
            return H_idx;
        }
        else
        {
            H_idx--;
        }
    }
}