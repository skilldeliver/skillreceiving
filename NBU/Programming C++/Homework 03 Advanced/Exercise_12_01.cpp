#include <iostream>
#include <cmath>

using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
    // finds distance between two points
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int main()
{
    double x, y;

    cout << "Enter x: "; cin >> x;
    cout << "Enter y: "; cin >> y;

    if (x >= -2 and x <= -1 and y >= 1 and y <= -1 and dist(x, y, 1, 1) > 1)
    {
        cout << "The point lies in the area";
    }
    else
        {
        cout << "The point is not in the area";
        }
}