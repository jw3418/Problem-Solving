#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    
    for (int i = lost.size() - 1; i >= 0; --i)
    {
        for (int j = reserve.size() - 1; j >= 0; --j)
        {
            if (lost[i] == reserve[j])
            {
                lost.erase(lost.begin() + i);
                reserve.erase(reserve.begin() + j);
                break;
            }
        }
    }
    
    set<int> reserve_set(reserve.begin(), reserve.end());
    set<int> already;
    int ans = n;
    
    for (int i = 0; i < lost.size(); ++i)
    {
        if (reserve_set.find(lost[i] - 1) != reserve_set.end())
        {
            reserve_set.erase(lost[i] - 1);
        }
        else if (reserve_set.find(lost[i] + 1) != reserve_set.end())
        {
            reserve_set.erase(lost[i] + 1);
        }
        else
        {
            ans--;
        }
    }
    
    return ans;
}