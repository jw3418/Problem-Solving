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
	for (int i = 1; i <= N; ++i)
	{
		vector<string> words;
		string line; getline(cin, line); 

		string cur;
		for (char c : line)
		{
			if (c == ' ')
			{
				if (!cur.empty())
				{
					words.push_back(cur);
					cur.clear();
				}
			}
			else
			{
				cur += c;
			}
		}
		if (!cur.empty())
		{
			words.push_back(cur);
		}

		string answer;
		for (int i = words.size()-1; i >= 0; --i)
		{
			answer += words[i] + " ";
		}

		cout << "Case #" << i << ": " << answer << endl;
	}

    return 0;
}
