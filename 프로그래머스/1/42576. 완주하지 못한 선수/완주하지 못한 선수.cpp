#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
//     map<string, int> Cnt;
//     for (auto it = completion.begin(); it != completion.end(); ++it)
//     {
//         if (Cnt.find(*it) != Cnt.end())
//         {
//             Cnt[*it] += 1;
//         }
//         else
//         {
//             Cnt[*it] = 1;
//         }
//     }
    
//     string answer = "";
//     for (auto &name : participant)
//     {
//         if ((Cnt.find(name) != Cnt.end()) && (Cnt[name] != 0)){
//             Cnt[name] -= 1;
//         }
//         else{
//             answer += name;
//             break;
//         }
//     }
    
    string answer = "";
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for (int i = 0; i < completion.size(); i++)
    {
        if (participant[i] != completion[i])
        {
            return participant[i];
        }
    }
    
    return participant[completion.size()];
}
            