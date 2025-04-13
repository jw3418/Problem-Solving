#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> one = {1, 2, 3, 4, 5};
    vector<int> two = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    vector<int> sum = {0, 0, 0};
    for (int i = 0; i < answers.size(); ++i)
    {
        if (answers[i] == one[i % 5])
        {
            sum[0]++;
        }
        if (answers[i] == two[i % 8])
        {
            sum[1]++;
        }
        if (answers[i] == three[i % 10])
        {
            sum[2]++;
        }
    }
    
    vector<int> result;
    int max_sum = *max_element(sum.begin(), sum.end());
    for (int i = 0; i < 3; ++i)
    {
        if (sum[i] == max_sum)
        {
            result.push_back(i+1);
        }
    }
    
    return result;
}