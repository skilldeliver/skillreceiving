#include <iostream>
#include <string>

using namespace std;

int main()
{
    int a, b, c;

    cout << "Enter the first number: "; cin >> a;
    cout << "Enter the second number: "; cin >> b;
    cout << "Enter the third number: "; cin >> c;

    if (c >= a)
    {
        if (a >= b) cout << c << " " << a << " " << b;
        else cout << c << " " << b << " " << a;
    }
    else if (b >= c)
    {
        if (a >= c) cout << b << " " << a << " " << c;
        else cout << b << " " << c << " " << a;
    }
    else
        {
            if (c >= b) cout << a << " " << c << " " << b;
            else cout << a << " " << b << " " << c;
        }

    return 0;
}