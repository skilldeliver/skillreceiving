
#include <iostream>
#include <cmath>

using namespace std;

double area(int x1, int y1, int x2, int y2, int x3, int y3)
{
    double a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    double b = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));
    double c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
    return (1.0/4) * sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));
}

bool in(int x, int y, int x1, int y1, int x2, int y2, int x3, int y3)
{
    double S = area (x1, y1, x2, y2, x3, y3);
    double S1 = area (x, y, x2, y2, x3, y3);
    double S2 = area (x1, y1, x, y, x3, y3);
    double S3 = area (x1, y1, x2, y2, x, y);

    return (S == S1 + S2 + S3);
}

int main()
{
    int x, x1, x2, x3, y, y1, y2, y3;
    cout << "Enter  point x: ";
    cin >> x;

    cout << "Enter  point y: ";
    cin >> y;

    cout << "Enter triangle A x: ";
    cin >> x1;

    cout << "Enter triangle A y: ";
    cin >> y1;

    cout << "Enter triangle B x: ";
    cin >> x2;

    cout << "Enter triangle B y: ";
    cin >> y2;

    cout << "Enter triangle C x: ";
    cin >> x3;

    cout << "Enter triangle C y: ";
    cin >> y3;

    if (in(x, y, x1, y1, x2, y2, x3, y3))
        cout << "The point is in the triangle";
    else
        cout << "The point is outside of the triangle";
}