#include <iostream>
#include <cmath>
#include <string>

using namespace std;

bool is_summed(int num, int n)
{
    // checks if num is the sum of the digits n powered
    string s = to_string(num);
    int sum = 0;

    for (int i = 0; i < s.size(); ++i) {
     sum += (int)pow(s[i] - 48, n);
    }

    return num == sum;
}

int main()
{

    int n;
    cout << "Enter n: "; cin >> n;

    for (int i = (int)pow(10, n - 1); i < (int)pow(10, n); ++i) {
        if (is_summed(i, n))
        {
            cout << i << endl;
        }
    }
}