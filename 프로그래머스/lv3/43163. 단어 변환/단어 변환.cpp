#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

int N, M;

int bfs(string begin, string target, vector<string> &words){
    queue<pair<string, int>> queue;
    queue.push({begin, 0});
    
    set<string> visit;
    visit.insert(begin);
    
    while (!queue.empty()){
        string curr = queue.front().first;
        int depth = queue.front().second;
        queue.pop();
        
        if (curr == target){
            return depth;
        }
        
        for (int i=0; i<N; i++){
            int check = 0;
            for (int j=0; j<M; j++){
                if (curr[j] == words[i][j]) check++;
            }
            if (check == M-1){
                visit.insert(words[i]);
                queue.push({words[i], depth+1});
            }
        }
    }
    return 0;
}

int solution(string begin, string target, vector<string> words) {
    N = words.size();
    M = words[0].length();
    
    auto it = find(words.begin(), words.end(), target);
    if (it == words.end()) return 0;
    
    int answer = bfs(begin, target, words);
    return answer;
}