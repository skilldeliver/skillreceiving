#include <iostream>

using namespace std;

int main()
{
    double a1, b1, c1, a2, b2, c2;

    cout << "Enter a1: "; cin >> a1;
    cout << "Enter b1: "; cin >> b1;
    cout << "Enter c1: "; cin >> c1;
    cout << "Enter a2: "; cin >> a2;
    cout << "Enter b2: "; cin >> b2;
    cout << "Enter c2: "; cin >> c2;

    // чрез правилото на Крамер
    double x = ((b2 * c1) - (b1 * c2)) / ((b2*a1)-(b1*a2));
    double y = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2*b1));

    cout << "x is: " << x << "\ny is: " << y << endl;
}