#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b){
    if (a[0] > b[0]){
        return true;
    }
    else if (a[0] == b[0]){
        return a[1] < b[1];
    }
    else{
        return false;
    }
}

int solution(vector<vector<int>> scores) {
    int answer = 1;
    
    int target_a = scores[0][0];
    int target_b = scores[0][1];
    int target_score = target_a + target_b;
    sort(scores.begin(), scores.end(), cmp);
    int max_b = 0;
    
    for (int i=0; i<scores.size(); i++){
        if (target_a < scores[i][0] && target_b < scores[i][1]){
            return -1;
        }
        if (max_b <= scores[i][1]){
            max_b = scores[i][1];
            if (scores[i][0] + scores[i][1] > target_score){
                answer++;
            }
        }
    }
    
    return answer;
}