#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double i = pow(a, 2) + pow(b, 2) + pow(c, 2);
	i =  (a + b) / (c + d);
	i = ((a + b) / c) * d;
	i = (a + b)/(c * d);
	i = (1 + (2 * 1.0) + (3 * 2 * 1)) / (1 + (1.0/(2 * 1) + (1.0/(3 * 2 * 1))));
	i = (sqrt(2) + sqrt(3) + sqrt(4)) / (sqrt(5) + sqrt(6) + sqrt(7));
	i = sin(x) + cos(x) - (pow(tan(x) + (1/(tan(x))), 3) / log(2 + pow(x, 4)));
	i = log(5) / log(2) + log(7) / log(3) + log(9) / log(5);
	i = pow(log(0) * abs(x) + pow(e, x-1), 3) / log(2 + pow(e, (x+y)/2));
	i = pow(pow(abs(x) + abs(y), 2) + pow(abs(x) + abs(y), 2), 3);
	i = asin(x) +  (pow(atan(x) + (1 / atan(x)), 3) / ((log(abs(2 + pow(x, 3)))) / log(2)) + 10);
	i = (sinh(x) + cosh(x)) / 2;
    return 0;
}