#include <iostream>

using namespace std;

int main()
{
    int x;
    cin >> x;

    bool is_power_of_two = !(x == 0) && !(x & (x - 1));
    cout << is_power_of_two;
}