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

    if (not(n >= 0 and n <= 9))
    {
        cout << "Invalid digit" << endl;
        return 0;
    }

    for (int i = 0; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            cout << j;
        }

        print('0', (n - i) * 2);

        for (int j = i; j >= 1; --j) {
            cout << j;
        }

        cout << endl;
    }
}