#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a, b, c;

    cout << "Enter a: "; cin >> a;
    cout << "Enter b: "; cin >> b;
    cout << "Enter c: "; cin >> c;

    double first_max = max(pow(a, 2) - pow(b, 3) + c, a - (4.5 * b));
    cout << "Answer: " << max(first_max, (1.5 * a) + (3.5 * b) - (8 * c)) - 7.5 << endl;
}