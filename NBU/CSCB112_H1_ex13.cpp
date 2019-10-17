#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	double pi = 3.14159;
	int x1, x2, x3, y1, y2, y3;

	cout << "Point 1 x: ";
	cin >> x1;

	cout << "Point 1 y: ";
	cin >> y1;

	cout << "Point 2 x: ";
	cin >> x2;

	cout << "Point 2 y: ";
	cin >> y2;

	cout << "Point 3 x: ";
	cin >> x3;

	cout << "Point 3 y: ";
	cin >> y3;

	double a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
	double b = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));
	double c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));

	double d = (2 * a * b * c) / sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));
	double r = d / 2;

	cout << "The circle area is: " <<  pi * r * r << "\n";
	cout << "The circle perimeter is: " << 2 * pi * r << "\n";
}