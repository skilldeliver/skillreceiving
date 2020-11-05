#include <iostream>
#include <cmath>

using namespace std;

double calc(double i, double x, int to)
{
    if (i == to * 2) return pow(x, 2);
    return pow(x, 2) + i / calc(i * 2, x, to);

}

int main()
{
    double x;
    cout << "Enter x: "; cin >> x;
    cout << x / calc(2, x, 256) << endl;
}