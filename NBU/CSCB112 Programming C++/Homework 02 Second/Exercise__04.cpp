#include <iostream>
#include <string>

using namespace std;

int main()
{
    int number, base;

    cout << "Enter number: "; cin >> number;
    cout << "Enter base: "; cin >> base;

    string converted_num;

    while (number != 0)
    {
        converted_num = to_string(number % base) + converted_num;
        number /= base;
    }
    cout << "Final number: " << converted_num << endl;

    return 0;
}