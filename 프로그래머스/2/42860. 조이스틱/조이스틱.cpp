#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(string name) {
    // 알파벳 바꾸기 위한 상하 횟수
    // 커서 이동을 위한 좌우 횟수
    int N = name.length();
    int answer = 0;
        
    for (int i = 0; i < N; ++i)
    {
        answer += min(name[i] - 'A', 'Z' - name[i] + 1);
    }
    
    int move = N - 1;   //그냥 오른쪽으로 쭉 가는 경우
    for (int i = 0; i < N; ++i)
    {
        int next = i + 1;
        while (next < N && name[next] == 'A')
        {
            next++;
        }
        move = min(move, i + i + (N - next));
        move = min(move, (N - next) + (N - next) + i);
    }
    answer += move;
    
    return answer;
}