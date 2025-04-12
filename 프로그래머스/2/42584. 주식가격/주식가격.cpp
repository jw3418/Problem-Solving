#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    int N = prices.size();
    
    vector<int> result;
    for (int i = 0; i < N-1; ++i)
    {
        int cnt = 0;
        for (int j = i; j < N-1; ++j)
        {
            if (prices[i] <= prices[j])
            {
                cnt++;
            }
            else
            {
                break;
            }
        }
        result.push_back(cnt);
    }
    result.push_back(0);
    
    return result;
}