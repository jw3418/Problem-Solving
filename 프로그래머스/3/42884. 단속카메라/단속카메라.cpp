#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
    
    sort(routes.begin(), routes.end(), [](const vector<int> &a, const vector<int> &b)
         {
             return a[1] < b[1];
         });
    
    int cnt = 0;
    int prev_camera = -30001;
    for (int i = 0; i < routes.size(); ++i)
    {
        if (routes[i][0] > prev_camera)
        {
            cnt++;
            prev_camera = routes[i][1];
        }
    }
    
    return cnt;
}