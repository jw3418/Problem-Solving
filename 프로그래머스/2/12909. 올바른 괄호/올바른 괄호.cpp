#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(string s)
{
    vector<char> Stack;
    for (int i = 0; i < s.length(); ++i)
    {
        if (s[i] == '(')
        {
            Stack.push_back(s[i]);
        }
        else
        {
            if (!Stack.empty() && Stack.back() == '(')
            {
                Stack.pop_back();
            }
            else
            {
                return false;
            }
        }
    }
    
    if (!Stack.empty())
    {
        return false;
    }
    return true;
}