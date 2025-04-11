#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    int PN = nums.size() / 2;
    
    set<int> nums_set(nums.begin(), nums.end());
    
    if (nums_set.size() <= PN)
    {
        return nums_set.size();
    }
    else
    {
        return PN;
    }
}