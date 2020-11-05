#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    if (not(n >= 10 and n <= 1010))
    {
        cout << "The number must be in 10-1010 range" << endl;
        return 0;
    }

    int count = 0;

    do {
        int digit = n % 2;

        if (digit != 0)
        {
            cout << "2^" << count << " + ";
        }
        count++;
        n /= 2;
    } while (n > 0);

    cout << "0" << endl;

    return 0;
}