#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a, b, c;

    cout << "Enter a: "; cin >> a;
    cout << "Enter b: "; cin >> b;
    cout << "Enter c: "; cin >> c;

    cout << "Answer: " << min(a+b+c, a*b*c) + 1.5 << endl;
}