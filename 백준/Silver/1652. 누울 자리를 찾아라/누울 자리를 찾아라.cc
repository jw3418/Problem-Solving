#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	int N; cin >> N; cin.ignore();
	vector<vector<char>> board(N, vector<char>(N, '.'));
	for (int i = 0; i < N; ++i)
	{
		string line; getline(cin, line);
		for (int j = 0; j < N; ++j)
		{
			board[i][j] = line[j];
		}
	}

	int hori = 0; int vert = 0;
	for (int i = 0; i < N; ++i)
	{
		int cnt = 0;
		for (int j = 0; j < N; ++j)
		{
			if (board[i][j] == '.')
			{
				cnt++;
			}
			else
			{
				cnt = 0;
			}
			if (cnt == 2)
			{
				hori++;
			}
		}
	}

	for (int j = 0; j < N; ++j)
	{
		int cnt = 0;
		for (int i = 0; i < N; ++i)
		{
			if (board[i][j] == '.')
			{
				cnt++;
			}
			else
			{
				cnt = 0;
			}
			if (cnt == 2)
			{
				vert++;
			}
		}
	}

	cout << hori << " " << vert << endl;

	return 0;
}