#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, score, P;
    cin >> N >> score >> P;

    vector<int> scores(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> scores[i];
    }
    scores.push_back(score);

    sort(scores.begin(), scores.end(), greater<int>());

    int rank = 1;
    for (int i = 0; i < scores.size(); ++i)
    {
        if (scores[i] > score)
            rank++;
        else
            break;
    }

	int same_cnt = 0;
	for (int i = scores.size()-1; i >= 0; --i)
	{
		if (scores[i] == score)
		{
			same_cnt++;
		}
		else
		{
			break;
		}
	}

    if (scores.size() > P)
    {
        if (rank + same_cnt > P)
            cout << -1 << endl;
        else
            cout << rank << endl;
    }
    else
    {
        cout << rank << endl;
    }

    return 0;
}
