#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    
    string answer = "";
    vector<char> stack;
    
    for (char ch : number)
    {
        while (!stack.empty() && k > 0 && stack.back() < ch)
        {
            stack.pop_back();
            --k;
        }
        stack.push_back(ch);
    }
    
    while (k > 0)
    {
        stack.pop_back();
        --k;
    }
    
    for (char ch : stack)
    {
        answer += ch;
    }
    
    
    return answer;
}