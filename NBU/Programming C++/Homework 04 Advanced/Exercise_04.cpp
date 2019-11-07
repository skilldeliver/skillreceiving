#include <iostream>

using namespace std;

int main()
{
    int n; int m;
    cin >> n;
    cin >> m;

    int sum = (m + n) * (m - n) / 2;
    int divider = 2;

    while (sum != 1)
    {
        if (sum % divider == 0)
        {
            sum /= divider;
            cout << divider;
            if (sum != 1) cout << " . ";
        }
        else
            divider++;
    }

    return 0;
}