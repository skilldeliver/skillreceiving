#include <iostream>
#include <string>

using namespace std;

int main()
{
    int age, days, hours, minutes;
    cout << "Enter age: "; cin >> age;

    days = age * 365;
    hours = days * 24;
    minutes = hours * 60;

    cout << "Days lived: " << days << endl;
    cout << "Hours lived: " << hours << endl;
    cout << "Minutes lived: " << minutes << endl;
}