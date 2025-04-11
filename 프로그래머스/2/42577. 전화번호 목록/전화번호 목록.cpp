#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

bool solution(vector<string> phone_book) {
    
    set<string> set_;
    for (int i = 0; i < phone_book.size(); ++i)
    {
        set_.insert(phone_book[i]);
    }
    
    for (int i = 0; i < phone_book.size(); ++i)
    {
        string number = "";
        for (int j = 0; j < phone_book[i].size(); ++j)
        {
            number += phone_book[i][j];
            if ((set_.find(number) != set_.end()) && (phone_book[i] != number))
            {
                return false;
            }
        }
    }
    
    return true;
}