#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	bool i = (n % 3 == 0 and n % 5 == 0) or (n % 2 == 0 and n % 7 == 0);
	i = sqrt(pow(b, 2) - (4 * a * c)) >= 0;
	i = sqrt(pow(a + 1, 2) + pow(b - 2, 2)) > 5;
	i = (a >= 0 and b >= 0) and sqrt(pow(a - 1, 2) + pow(b - 1, 2)) > 7
	i = sqrt(pow(a, 2) + pow(b, 2)) < 1 or sqrt(pow(a, 2) + pow(b, 2)) > 5;
	i = x >= a and x <= b;
	i = x == min(a, min(b, c));
	i = x != min(a, min(b, c));
	i = (!x) and (!y);
	i = a > 0 or b > 0 or c > 0;
	i = std::to_string(n).find("5") != std::string::npos;
	i = n[0] == n[1] or n[0] == n[2] or n[0] == n[3] or n[1] == n[2] or n[1] == n[3] or n[2] == n[3];
	return 0;
}