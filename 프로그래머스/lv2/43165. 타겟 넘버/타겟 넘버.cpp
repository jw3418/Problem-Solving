#include <iostream>
#include <vector>
using namespace std;

int way_cnt = 0;

void dfs(string operatorStr, int depth, const vector<int>& numbers, int target) {
    if (depth == numbers.size() - 1) {
        int tmp_sum = 0;
        for (int i = 0; i < numbers.size(); ++i) {
            if (operatorStr[i] == '+') {
                tmp_sum += numbers[i];
            } else {
                tmp_sum -= numbers[i];
            }
        }
        if (tmp_sum == target) {
            way_cnt++;
        }
        return;
    }

    dfs(operatorStr + '+', depth + 1, numbers, target);
    dfs(operatorStr + '-', depth + 1, numbers, target);
}

int solution(vector<int> numbers, int target) {
    dfs("+", 0, numbers, target);
    dfs("-", 0, numbers, target);
    return way_cnt;
}