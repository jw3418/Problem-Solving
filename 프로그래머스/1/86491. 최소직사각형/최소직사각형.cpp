#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(vector<vector<int>> sizes) {
    
    int W = sizes[0][0]; int H = sizes[0][1];
    for (int i = 1; i < sizes.size(); ++i)
    {
        vector<int> size = sizes[i];
        if ((abs(W - size[0]) + abs(H - size[1])) < (abs(W - size[1]) + abs(H - size[0])))
        {
            W = max(W, size[0]); H = max(H, size[1]);
        }
        else
        {
            W = max(W, size[1]); H = max(H, size[0]);
        }
    }
    
    return W * H;
}