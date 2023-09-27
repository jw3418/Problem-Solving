#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

#define INF INT_MAX
#define MAX 100000

int N, S;
int nums[MAX];

int main() {
    cin >> N;
    cin >> S;

    for (int i=0; i<N; i++){
        cin >> nums[i];
    }

    int left = 0;
    int right = 0;
    int sum = 0;
    int length = INT_MAX;

    while (1){
        if (sum >= S){
            length = min(length, right - left);
            sum -= nums[left];
            left++;
        }
        else if (right == N){
            break;
        }
        else{
            sum += nums[right];
            right++;
        }
    }

    if (length == INT_MAX){
        cout << 0;
    }
    else{
        cout << length;
    }

    return 0;
}