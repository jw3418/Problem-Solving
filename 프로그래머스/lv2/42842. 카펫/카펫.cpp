#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int width = 3; int height = 1;
    int total = brown + yellow;
    
    while (1){
        height = (int)total / width;
        
        if (total % width == 0 && width >= height && (width-2)*(height-2) == yellow){
            answer.push_back(width); answer.push_back(height);
            return answer;
        }
        
        width++;
    }
}