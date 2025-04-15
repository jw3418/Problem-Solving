#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <iostream>

using namespace std;

bool isPrime(int number)
{
    if (number == 1)
    {
        return false;
    }
    if (number == 2)
    {
        return true;
    }
    if (number % 2 == 0)
    {
        return false;
    }
    
    for (int i = 2; i <= sqrt(number); i++)
    {
        if (number % i == 0)
        {
            return false;
        }
    }
    return true;
}

int solution(string numbers) {
    
    sort(numbers.begin(), numbers.end(), [](const int &a, const int &b)
         {
            return a < b; 
         });
    
    set<int> result;
    do
    {
        for (int i = 1; i <= numbers.size(); ++i)
        {
            string sub = numbers.substr(0, i);
            if (isPrime(stoi(sub)))
            {
                result.insert(stoi(sub));
            }
        }
    }
    while (next_permutation(numbers.begin(), numbers.end()));
    
    return result.size();
}