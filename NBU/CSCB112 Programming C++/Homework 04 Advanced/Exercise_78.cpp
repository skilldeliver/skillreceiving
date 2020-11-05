#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int period_start(int num)
{
    string s = to_string(1.0 / num);
    return s[2] - 48;
}

int main()
{
    int num;
    cout << "Enter the number: "; cin >> num;
    cout << period_start(num);
}