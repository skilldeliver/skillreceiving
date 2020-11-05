#include <iostream>
#include <cmath>

using namespace std;

int main()
{
double a;
cout << "Please enter the triangle side: ";
cin >> a;

cout << "The triangle area is: " <<  (sqrt(3)/4) * pow(a, 2) << "\n";
cout << "The triangle perimeter is: " << 3 * a << "\n";
}