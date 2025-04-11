#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    unordered_map<string, vector<string>> map_;
    
    for (auto it = clothes.begin(); it < clothes.end(); ++it)
    {
        map_[(*it)[1]].push_back((*it)[0]);
    }
    
    for (const auto &map : map_)
    {
        for (int i = 0; i < map.second.size(); i++)
        {
            cout << map.second[i] << " ";
        }
        cout << endl;
    }
    
    int answer = 1;
    for (const auto &map : map_)
    {
        answer *= (map.second.size() + 1);
    }
    answer -= 1;
    
    return answer;
}