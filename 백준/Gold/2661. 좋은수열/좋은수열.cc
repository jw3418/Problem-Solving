#include <iostream>
#include <string>
using namespace std;

int N;
string seq;
bool done = false;

bool check_curr(string seq){
    int n = seq.size();
    for (int i=1; i<=int(n/2); i++){
        if (seq.substr(n-i, i) == seq.substr(n-2*i, i)){ //substr(시작인덱스, 문자열길이)
            return false;
        }
    }
    return true;
}

void backtracking(string seq){
    if (done) return;
    if (seq.size() == N){
        cout << seq;
        done = true;
    }
    else{
        for (int i=1; i<3+1; i++){
            if (check_curr(seq+to_string(i))){ //int -> string to_string 사용
                backtracking(seq+to_string(i)); 
            }
        }
    }
}

int main() {
    cin >> N;
    backtracking("1");

    return 0;
}