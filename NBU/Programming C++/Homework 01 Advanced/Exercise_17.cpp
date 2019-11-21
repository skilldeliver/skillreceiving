#include <iostream>
#include <string>

using namespace std;

int main()
{
    int x, k;

    cin >> x;
    cin >> k;
    cout << to_string(x)[k + 1];
}