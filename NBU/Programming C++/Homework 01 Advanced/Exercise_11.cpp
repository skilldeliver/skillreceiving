#include <iostream>

using namespace std;

int main()
{
    double pi = 3.14159;
    double r;
    cout << "Please enter circle radius: ";
    cin >> r;

    cout << "The circle area is: " <<  pi * r * r << "\n";
    cout << "The circle perimeter is: " << 2 * pi * r << "\n";
}