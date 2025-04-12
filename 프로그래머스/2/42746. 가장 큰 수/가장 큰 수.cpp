#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    
    sort(numbers.begin(), numbers.end(), [](const int &a, const int &b)
         {
             string sa = to_string(a) + to_string(b); 
             string sb = to_string(b) + to_string(a);
             return sa > sb;
         });
    
    string result = "";
    for (int i = 0; i < numbers.size(); ++i)
    {
        result += to_string(numbers[i]);
    }
    
    if (result[0] == '0')
    {
        return "0";
    }
    return result;
}