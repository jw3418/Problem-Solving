#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool match(string &t, int i, string &s)
{
    int len = s.length();
    if (i < len) return false;
    for (int j = 0; j < len; ++j)
    {
        if (t[i - len + j] != s[j])
        {
            return false;
        }
    }
    return true;
}

int solution(vector<string> strs, string t)
{
    
    vector<int> dp(t.size()+1, 1e9);
    dp[0] = 0;
    
    for (int i = 1; i <= t.size(); ++i)
    {
        for (string str : strs)
        {
            if (match(t, i, str))
            {
                dp[i] = min(dp[i], dp[i-str.length()]+1);
            }
        }
    }
    
    if (dp[t.size()] == 1e9)
    {
        return -1;
    }
    else
    {
        return dp[t.size()];
    }
}