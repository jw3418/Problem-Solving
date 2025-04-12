#include <string>
#include <vector>
#include <deque>
#include <numeric>
#include <iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    deque<int> Truck(truck_weights.begin(), truck_weights.end());
    deque<int> Bridge;   //무게, 경과시간
    int BSum = 0;
    
    int seconds = 0;
    while (!Truck.empty())
    {        
        if (Bridge.size() == bridge_length)
        {
            BSum -= Bridge.front();
            Bridge.pop_front();
        }
        if (Bridge.size() < bridge_length)
        {
            if ((weight - BSum) >= Truck.front())
            {
                Bridge.push_back(Truck.front());
                BSum += Truck.front();
                Truck.pop_front();
            }
            else
            {
                Bridge.push_back(0);
            }
        }

        seconds++;
    }
    
    seconds += bridge_length;
    return seconds;
}