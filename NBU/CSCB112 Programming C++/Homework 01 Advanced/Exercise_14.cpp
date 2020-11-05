#include <iostream>
#include <string>
#include <cmath>

using namespace std;
int main()
{

    int x1, x2, x3, x4, y1, y2, y3, y4;
    double h;
    string type;

    cout << "Choose prism. Type triangle or quadrangular: ";
    cin >> type;

    if (type == "triangle" or type == "quadrangular")
    {
        cout << "Point 1 x: ";
        cin >> x1;

        cout << "Point 1 y: ";
        cin >> y1;

        cout << "Point 2 x: ";
        cin >> x2;

        cout << "Point 2 y: ";
        cin >> y2;

        cout << "Point 3 x: ";
        cin >> x3;

        cout << "Point 3 y: ";
        cin >> y3;
    }
    if (type == "quadrangular")
    {
        cout << "Point 4 x: ";
        cin >> x4;

        cout << "Point 4 y: ";
        cin >> y4;
    }
    else if (type != "triangle")
        {
        cout << "Not a valid prism type!";
        return 0;
        }

    cout << "Enter the prism height: ";
    cin >> h;

    double a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    double b = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));
    double c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
    double B = (1.0/4) * sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));

    if (type == "quadrangular")
    {	
        c = sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2));
        double d = sqrt(pow(x4 - x1, 2) + pow(y4 - y1, 2));
        double p = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));
        double q = sqrt(pow(x2 - x4, 2) + pow(y2 - y4, 2));
        B = (1.0/4) * sqrt(4 * pow(p, 2) * pow(q, 2) - pow((pow(a, 2) + pow(c, 2) - pow(b, 2) - pow(d, 2)), 2));
    }

    cout << "The area of the " << type << " prism is: " << B * h;
}