#include <iostream>
#include <string>
#include <cmath>
#include <math.h>

using namespace std;

int main()
{
    double circle_radius, square_side, rect_a, rect_b, triangle_a, triangle_b;
    cout << "Enter the circle radius: "; cin >> circle_radius;
    cout << "The circle perimeter is: " << 2 * circle_radius * M_PI << endl
         << "The circle area is: " << M_PI * pow(circle_radius, 2) << endl;

    cout << "Enter the square side: "; cin >> square_side;
    cout << "The square perimeter is: " << square_side * 4 << endl
         << "The square area is: " << square_side * square_side << endl;

    cout << "Enter the rectangle a side: "; cin >> rect_a;
    cout << "Enter the rectangle b side: "; cin >> rect_b;
    cout << "The rectangle perimeter is: " << (2 * rect_a) + (2 * rect_b) << endl
         << "The rectangle area is: " << rect_a * rect_b << endl;

    cout << "Enter the triangle a side: "; cin >> triangle_a;
    cout << "Enter the triangle b side: "; cin >> triangle_b;
    cout << "The triangle perimeter is: " << triangle_a + triangle_b + sqrt(pow(triangle_a, 2) + pow(triangle_b, 2)) << endl
         << "The triangle area is: " << (rect_a * rect_b) / 2.0 << endl;
}