#include <iostream>
#include <vector>
#include <queue>
using namespace std;


int main() {
    int N; cin >> N;

    priority_queue<int, vector<int>, greater<int>> Q;
    int mx = 0;
    for (int i=0; i<N; i++){
        int v; cin >> v;
        mx = max(mx, v);
        Q.push(v);
    }

    int curr_mx = mx;
    int diff = curr_mx - Q.top();

    while (Q.top() < mx){
        int v = Q.top(); Q.pop();
        diff = min(diff, curr_mx - v);
        curr_mx = max(curr_mx, v*2);
        Q.push(v*2);
    }

    cout << min(curr_mx - Q.top(), diff);

    return 0;
}