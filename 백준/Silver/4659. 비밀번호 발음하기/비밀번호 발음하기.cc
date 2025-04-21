#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

int main()
{
	set<char> moum = {'a', 'e', 'i', 'o', 'u'};
	
	while (true)
	{
		string password; cin >> password; cin.ignore();
		if (password == "end") break;

		bool one = false; bool two = true; bool three = true;
		int m_cnt = 0; int j_cnt = 0;
		char prev = ' ';
		for (int i = 0; i < password.length(); ++i)
		{
			if (moum.find(password[i]) != moum.end())
			{
				one = true;
				j_cnt = 0; m_cnt++;
			}
			else
			{
				m_cnt = 0; j_cnt++;
			}

			if (m_cnt >= 3 || j_cnt >= 3)
			{
				two = false;
			}

			if (prev == password[i])
			{
				if (prev != 'e' && prev != 'o')
				{
					three = false;
				}
			}

			prev = password[i];
		}

		string ans = "<";
		if (one && two && three)
		{
			ans += password;
			ans += "> is acceptable.\n";
		}
		else
		{
			ans += password;
			ans += "> is not acceptable.\n";
		}
		cout << ans;
	}

	return 0;
}