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
    int num, result;

    cout << "Enter a number: "; cin >> num;

    for (int c = 31; c >= 0; c--)
    {
        result = num >> c;

        if (result & 1)
            cout << "1";
        else
            cout << "0";
    }
    return 0;
}