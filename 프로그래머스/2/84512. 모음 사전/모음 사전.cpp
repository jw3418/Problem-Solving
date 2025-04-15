#include <string>
#include <vector>

using namespace std;

int count = 0;
bool found = false;
vector<char> vowels = {'A', 'E', 'I', 'O', 'U'};

bool dfs(string current, const string& target) {
    count++;

    if (current == target) {
        found = true;
        return true;
    }
    if (current.length() == 5) return false;

    for (char v : vowels) {
        if (dfs(current + v, target)) return true;
    }

    return false;
}

int solution(string word) {
    count = 0;
    found = false;

    for (char v : vowels) {
        if (dfs(string(1, v), word)) break;
    }

    return count;
}
