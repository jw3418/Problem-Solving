#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	map<int, pair<int, int>> coor;
	for (int i = 0; i < 5; ++i)
	{
		for (int j = 0; j < 5; ++j)
		{
			int t; cin >> t;
			coor[t] = {i, j};
		}
	}

	vector<int> cmds;
	for (int i = 0; i < 25; ++i)
	{
		int t; cin >> t;
		cmds.push_back(t);
	}

	vector<vector<bool>> check(5, vector<bool>(5, false));
	int cnt = 0;
	for (auto cmd : cmds)
	{
		cnt++;
		int x = coor[cmd].first, y = coor[cmd].second;
		check[x][y] = true;

		/*빙고 검사*/
		int ans = 0;
		//1) 가로
		for (int i = 0; i < 5; ++i)
		{
			int tmp = 0;
			for (int j = 0; j < 5; ++j)
			{
				if (check[i][j])
				{
					tmp++;
				}
				else
				{
					break;
				}
			}
			if (tmp == 5)
			{
				ans++;
			}
		}

		//2) 세로
		for (int j = 0; j < 5; ++j)
		{
			int tmp = 0;
			for (int i = 0; i < 5; ++i)
			{
				if (check[i][j])
				{
					tmp++;
				}
				else
				{
					break;
				}
			}
			if (tmp == 5)
			{
				ans++;
			}
		}

		//3) 우하 대각선

		if (check[0][4] && check[1][3] && check[2][2] && check[3][1] && check[4][0])
		{
			ans++;
		}

		//4) 우상 대각선
		if (check[0][0] && check[1][1] && check[2][2] && check[3][3] && check[4][4])
		{
			ans++;
		}

		if (ans >= 3)
		{
			cout << cnt;
			break;
		}
	}

	return 0;
}