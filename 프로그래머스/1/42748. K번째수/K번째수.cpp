#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    
    vector<int> result;
    for (int t = 0; t < commands.size(); ++t)
    {
        vector<int> vec;
        for (int i = commands[t][0]-1; i <= commands[t][1]-1; ++i)
        {
            vec.push_back(array[i]);
        }
        sort(vec.begin(), vec.end());

        result.push_back(vec[commands[t][2]-1]);
    }
    
    return result;
}