#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    int N = genres.size();
    
    unordered_map<string, vector<vector<int>>> Counter;
    unordered_map<string, int> Sum;
    
    for (int i = 0; i < N; i++)
    {
        Counter[genres[i]].push_back({plays[i], i});
        Sum[genres[i]] += plays[i];
    }
    
    vector<pair<string, int>> GenreOrder(Sum.begin(), Sum.end());
    sort(GenreOrder.begin(), GenreOrder.end(), [](pair<string, int> &a, pair<string, int> &b)
         {
             return a.second > b.second;
         });
    
    for (auto &pair : Counter)
    {
        sort(pair.second.begin(), pair.second.end(), [](vector<int> &a, vector<int> &b)
            {
                if (a[0] == b[0])
                {
                    return a[1] < b[1];
                }
                return a[0] > b[0];
            });
    }
    
    vector<int> answer;
    for (auto &pair : GenreOrder)
    {
        int cnt = 0;
        for (auto &vec: Counter[pair.first])
        {
            if (cnt < 2)
            {
                answer.push_back(vec[1]);
                ++cnt;
            }
            else
            {
                break;
            }
        }
    }
    
    return answer;
}