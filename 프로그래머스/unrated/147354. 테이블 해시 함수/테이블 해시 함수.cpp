#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int column;

bool cmp(const vector<int>& v1, const vector<int>& v2){
    if (v1[column] == v2[column]){
        return v1[0] > v2[0] ? true : false;
    }
    else{
        return v1[column] < v2[column] ? true: false;
    }
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    column = col - 1;
    sort(data.begin(), data.end(), cmp);
    
    int answer = 0;
    int col_len = data[0].size();
    for (int i = row_begin; i <= row_end; i++){
        int totalSum = 0;
        for (int j = 0; j < col_len; j++){
            totalSum += (data[i-1][j] % i);
        }
        answer ^= totalSum;
    }
    return answer;
}