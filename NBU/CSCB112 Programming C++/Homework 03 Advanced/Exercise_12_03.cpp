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

    if (dist(x, y, 2, 2) <= 2 and dist(x, y, 2, 0) > 1)
    {
        cout << "The point lies in the area";
    }
    else
        {
        cout << "The point is not in the area";
        }
}