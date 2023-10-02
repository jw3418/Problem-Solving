#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int N;

void dfs(vector<char> path, int depth, int result){
    if (depth == N-1){
        if (result == 0){
            for (int i=0; i<path.size(); i++){
                cout << path[i];
            }
            cout << '\n';
        }
        return;
    }

    // 공백 연산
    vector<char> p1 = path;
    int n = depth+2;
    p1.push_back(' '); p1.push_back(n+'0');

    if(path.size() > 2){
        int idx = path.size()-2;
        if (path[idx] == '+'){
            dfs(p1, depth+1, result-(n-1)+(10*(n-1)+n));
        }
        else if (path[idx] == '-'){
            dfs(p1, depth+1, result+(n-1)-(10*(n-1)+n));
        }
    }
    else{
        dfs(p1, depth+1, 12);
    }

    // + 연산
    vector<char> p2 = path;
    p2.push_back('+'); p2.push_back(n+'0');
    dfs(p2, depth+1, result+n);

    // - 연산
    vector<char> p3 = path;
    p3.push_back('-'); p3.push_back(n+'0');
    dfs(p3, depth+1, result-n);
}

int main() {
    int T; cin >> T;
    for (int t=0; t<T; t++){
        cin >> N;
        vector<char> tmp; tmp.push_back('1');
        dfs(tmp, 0, 1);
        cout << '\n';
    }
    return 0;
}