#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	vector<vector<int>> board;
	for (int i = 0; i < 9; ++i)
	{
		vector<int> row;
		for (int j = 0; j < 9; ++j)
		{
			int tmp; cin >> tmp;
			row.push_back(tmp);
		}
		board.push_back(row);
	}

	int max_ = -1; int x, y;
	for (int i = 0; i < 9; ++i)
	{
		for (int j = 0; j < 9; ++j)
		{
			if (max_ < board[i][j])
			{
				max_ = board[i][j];
				x = i+1; y = j+1;
			}
		}
	}

	cout << max_ << endl;
	cout << x << " " << y;

	return 0;
}