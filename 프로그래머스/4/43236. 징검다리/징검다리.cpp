#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    
    rocks.push_back(distance);
    sort(rocks.begin(), rocks.end());
    
    long long left = 0; long long right = distance;
    
    while (left <= right)
    {
        long long mid = (left + right) / 2;
        
        long removed_cnt = 0;
        long long pre = 0;
        for (long i = 0; i < rocks.size(); ++i)
        {
            if ((rocks[i] - pre) < mid)
            {
                removed_cnt++;
            }
            else
            {
                pre = rocks[i];
            }
        }
        
        if (removed_cnt > n)
        {
            right = mid - 1;
        }
        else
        {
            answer = mid;
            left = mid + 1;
        }
    }
    
    return answer;
}