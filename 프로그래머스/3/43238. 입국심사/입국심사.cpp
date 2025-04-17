#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int N, vector<int> times) {
    
    long long answer = 0;
    
    long long left = 1; long long right = (long long)*max_element(times.begin(), times.end()) * N;
        
    while (left <= right)
    {
        long long mid = (left + right) / 2;
        long long cnt = 0;
        
        for (const auto time : times)
        {
            cnt += (long long)mid / time;
        }
        
        if (cnt >= N)
        {
            answer = mid;
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    
    return answer;
}