#include <iostream>

using namespace std;

int main()
{
    int a = 7;
    int b = 18;

    a = a + b;
    b = a - b;
    a = a - b;

    cout << a << " ";
    cout << b;

}