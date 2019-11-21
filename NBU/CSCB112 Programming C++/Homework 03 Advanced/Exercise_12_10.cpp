#include <iostream>
#include <cmath>

using namespace std;

double area(double x1, double y1, double x2, double y2, double x3, double y3)
{
    double a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    double b = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));
    double c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
    return (1.0/4) * sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));
}

bool in(double x, double y, double x1, double y1, double x2, double y2, double x3, double y3)
{
    double S = area (x1, y1, x2, y2, x3, y3);
    double S1 = area (x, y, x2, y2, x3, y3);
    double S2 = area (x1, y1, x, y, x3, y3);
    double S3 = area (x1, y1, x2, y2, x, y);

    return (S == S1 + S2 + S3);
}

int main()
{
    double x, y;

    cout << "Enter x: "; cin >> x;
    cout << "Enter y: "; cin >> y;

    if (in(x, y, -2, 1, 1, -2, 1, 1))
        cout << "The point lies in the area";
    else
        cout << "The point is outside of the area";
}