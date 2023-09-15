#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(vector<int> &a, vector<int> &b){
    return a[1] < b[1];
}

int solution(vector<vector<int>> targets) {
    
    sort(targets.begin(), targets.end(), cmp);
    
    // for (int i=0; i<targets.size(); i++){
    //     for (int j=0; j<targets[i].size(); j++){
    //         cout << targets[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }
    
    int curr = -1;
    int answer = 0;
    for (int i=0; i<targets.size(); i++){
        if (curr > targets[i][0] && curr <= targets[i][1]){
            continue;
        }
        else{
            curr = targets[i][1];
            answer++;
        }
    }
    
    return answer;
}