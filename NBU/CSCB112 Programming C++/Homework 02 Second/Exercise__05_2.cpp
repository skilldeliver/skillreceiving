#include <iostream>

#include <cmath>

using namespace std;

int main()
{
    int p;
    cout << "Enter equilateral triangle perimeter: "; cin >> p;
    cout << "The area of the triangle is: " << (sqrt(3) / 4) * pow(p/3.0,2);
    return 0;
}