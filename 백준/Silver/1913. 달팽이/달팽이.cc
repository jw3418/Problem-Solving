#include <iostream>
#include <vector>

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
	int N; cin >> N;
	int target; cin >> target;

	vector<vector<int>> board(N, vector<int>(N, 0));

	int x = 0; int y = 0;
	int num = N*N;
	int d = 0;
	int tx = -1; int ty = -1;

	while (num > 0)
	{
		board[x][y] = num;

		if (num == target)
		{
			tx = x+1;
			ty = y+1;
		}

		if (x+dx[d] < 0 || x+dx[d] >= N || y+dy[d] < 0 || y+dy[d] >= N
		|| board[x+dx[d]][y+dy[d]] != 0)
		{
			d = (d+1) % 4;
		}

		x += dx[d];
		y += dy[d];
		num--;
	}

	for (auto vec : board)
	{
		for (auto it : vec)
		{
			cout << it << " ";
		}
		cout << endl;
	}

	cout << tx << " " << ty << endl;

	return 0;
}