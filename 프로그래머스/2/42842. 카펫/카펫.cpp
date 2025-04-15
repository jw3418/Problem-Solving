#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int W = 3; int H = -1;
    int total = brown + yellow;
    
    while (1)
    {
        H = (int)total / W;
        if (((H-2) * (W-2) == yellow) && (total % W == 0) && (W >= H))
        {
            answer.push_back(W); answer.push_back(H);
            return answer;
        }
        W++;
    }
}