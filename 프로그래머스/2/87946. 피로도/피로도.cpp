#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    
    sort(dungeons.begin(), dungeons.end());
    
    int max_cnt = 0;
    do
    {
        int cnt = 0; int tk = k;
        for (int i = 0; i < dungeons.size(); ++i)
        {
            if ((tk >= dungeons[i][0]))
            {
                if (tk - dungeons[i][1] < 0)
                {
                    break;
                }
                tk -= dungeons[i][1];
                cnt++;
            }
        }
        max_cnt = max(max_cnt, cnt);
    }
    while(next_permutation(dungeons.begin(), dungeons.end()));
    
    return max_cnt;
}