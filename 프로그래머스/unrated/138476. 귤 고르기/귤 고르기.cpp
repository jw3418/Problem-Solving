#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(const pair<int, int> &a, const pair<int, int> &b){
    return a.second > b.second;
}

int solution(int k, vector<int> tangerine) {
    
    map<int, int> tcnt;
    for (int i=0; i<tangerine.size(); i++){
        auto it = tcnt.find(tangerine[i]);
        if (it != tcnt.end()){
            tcnt[tangerine[i]]++;
        }
        else{
            tcnt[tangerine[i]] = 1;
        }
    }
    
    vector<pair<int, int>> vec(tcnt.begin(), tcnt.end());
    sort(vec.begin(), vec.end(), cmp);
    
    // for (int i=0; i<vec.size(); i++){
    //     cout << vec[i].first << ',' << vec[i].second << ' ';
    // }
    
    int total = 0;
    int answer = 0;
    for (int i=0; i<vec.size(); i++){
        total += vec[i].second;
        answer++;
        if (total >= k){
            break;
        }
    }
    
    return answer;
}