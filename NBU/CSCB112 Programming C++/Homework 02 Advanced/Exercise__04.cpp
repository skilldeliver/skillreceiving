#include <iostream>

using namespace std;

int main()
{
    int num1, num2;

    cout << "Enter first number: "; cin >> num1;
    cout << "Enter second number: "; cin >> num2;

    while (num2 != 0)
    {
        int bits = num1 & num2;
        num1 = num1 ^ num2;
        num2 = bits << 1;
    }
    cout << num1;
} 