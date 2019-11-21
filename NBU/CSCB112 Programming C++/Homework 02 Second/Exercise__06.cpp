#include <iostream>

using namespace std;

int main()
{
	bool i = p % (4*7) == 0;
	bool i = (pow(b, 2) - (4 * a * c)) < 0;
	bool i = sqrt(pow(a, 2) + pow(b - 1, 2)) <= 5;
	bool i = sqrt(pow(a - c, 2) + pow(b - d, 2)) > f;
	bool i = sqrt(pow(a, 2) + pow(b, 2)) <= 5 and a < 0 and b < 0;
	bool i = sqrt(pow(a, 2) + pow(b, 2)) >= 5 and sqrt(pow(a, 2) + pow(b, 2)) <= 10;
	bool i = x >= 0 and x <= 1;
	bool i = x == max(max(a,b),c);
	bool i = x != max(max(a,b),c);
	bool i = x or y;
	bool i = x and y;
	bool i = a <= 0 and b <= 0 and c <= 0;
	bool i = (p % 10 == 7) or ((p / 10) % 10 == 7) or ((p / 100) % 10 == 7);	
	bool i = ((m / 100) % 10) != ((m / 10) % 10) and ((m / 100) % 10) != (m % 10) and ((m / 10) % 10) != (m % 10);
	bool i = ((m / 100) % 10) == ((m / 10) % 10) or ((m / 100) % 10) == (m % 10) or ((m / 10) % 10) == (m % 10);
	bool i = ((x % 10) < (x / 10) % 10 and ((x / 10) % 10 < (x / 100) % 10)) or ((x % 10) > (x / 10) % 10 and ((x / 10) % 10 > (x / 100) % 10));
	bool i = x == ((x % 10) * 100) + ((x / 10) % 10 * 10) + (x / 100) or y == ((y % 10) * 100) + ((y / 10) % 10 * 10) + (y / 100) or y == ((y % 10) * 100)
	bool i = x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23;
    return 0;
}