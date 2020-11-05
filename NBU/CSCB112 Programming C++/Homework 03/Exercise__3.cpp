#include <iostream>

#define MAX 10000000
#define MIN -100000000

using namespace std;

int main()
{
    int n = 0;
    cout << "Enter an integer: "; cin >> n;

    if (n >= MIN and n <= MAX)
        cout << "The integer is in the range";
    else
        cout << "The integer is not in the range";
    return 0;
}