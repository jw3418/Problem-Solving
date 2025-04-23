#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N; cin.ignore();
	int L; cin >> L; cin.ignore();
	string S; getline(cin, S);
	
	int cnt = 0;
	int ans = 0;
	for (int i = 1; i < L-1; ++i)
	{
		if (S[i] == 'O' && S[i-1] == 'I' && S[i+1] == 'I')
		{
			cnt++;
			if (cnt == N)
			{
				ans++;
				cnt--;
			}
			i++;
		}
		else
		{
			cnt = 0;
		}
	}
	cout << ans << endl;

    return 0;
}
