#include <iostream>
#include <string>

using namespace std;

void print(char let, int count)
{
    // prints the let count times
    for (int i = 0; i < count; ++i) {
        cout << let;
    }
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        print(' ', abs(i - (n - 1)));
        print('*', (i + 1) * 2 - 1);
        cout << endl;
    }
    return 0;
}