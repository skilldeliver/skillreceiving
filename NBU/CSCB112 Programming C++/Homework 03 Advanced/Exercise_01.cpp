#include <iostream>
#include <string>

using namespace std;

int main()
{
    int number, number_safe, base;

    cout << "Enter number: "; cin >> number;
    cout << "Enter base: "; cin >> base;
    number_safe = number;

    string converted_num;

    while (number != 0)
    {
        converted_num = to_string(number % base) + converted_num;
        number /= base;
    }
    cout << number_safe << "(10)=" << converted_num << "(" << base << ")" << endl;

    return 0;
}