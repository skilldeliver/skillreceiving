#include <iostream>
#include <cmath>
#include <string>

using namespace std;


void print_dict(double AB, double BC, double CD, double AD)
{
    cout << "Distance from AB: " << AB << endl;
    cout << "Distance from BC: " << BC << endl;
    cout << "Distance from CD: " << CD << endl;
    cout << "Distance from AD: " << AD << endl;
}


double dist(double x1, double y1, double x2, double y2)
{
    // finds distance between two points
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void calc_distances(double x,
                   double y,
                   pair<double, double> A,
                   pair<double, double> B,
                   pair <double, double> C,
                   pair<double, double> D)
{
    if (x >= A.first and x <= B.first and y >= A.second and y <= C.second) // checks if the point is in the square
    {
        print_dict(y - A.second, B.first - x, C.second - y, x - D.first);
     }
    else if (x >= A.first and x <= B.first) // point in x range
        {
            // the perpendicular distances
            cout << "Distance from AB: " << abs(y - A.second) << endl;
            cout << "Distance from CD: " << abs(y - C.second) << endl;

            if (y > C.second) // above the square
            {
                cout << "Distance from BC: " << dist(x, y, C.first, C.second) << endl;
                cout << "Distance from AD: " << dist(x, y, D.first, D.second) << endl;
            }
            else // under the square
                {
                    cout << "Distance from BC: " << dist(x, y, B.first, B.second) << endl;
                    cout << "Distance from AD: " << dist(x, y, A.first, A.second) << endl;
                }

        }
    else if (y >= A.second and y <= C.second) // point in y range
    {
        // the perpendicular distances
        cout << "Distance from AD: " << abs(x - A.first) << endl;
        cout << "Distance from BC: " << abs(x - B.first) << endl;

        if (x > C.first) // on the right
        {
            cout << "Distance from CD: " << dist(x, y, C.first, C.second) << endl;
            cout << "Distance from AB: " << dist(x, y, B.first, B.second) << endl;
        }
        else // on the left
        {
            cout << "Distance from CD: " << dist(x, y, D.first, D.second) << endl;
            cout << "Distance from AB: " << dist(x, y, A.first, A.second) << endl;
        }
    }
    else if (x < A.first and y > D.second)
        {
            print_dict(dist(x, y, A.first, A.second),
                       dist(x, y, C.first, C.second),
                       dist(x, y, D.first, D.second),
                       dist(x, y, D.first, D.second));
        }
    else if (x < A.first and y < A.second)
    {
        print_dict(dist(x, y, A.first, A.second),
                   dist(x, y, B.first, B.second),
                   dist(x, y, D.first, D.second),
                   dist(x, y, A.first, A.second));
    }
    else if (x > B.first and y > C.second)
    {
        print_dict(dist(x, y, B.first, B.second),
                   dist(x, y, C.first, C.second),
                   dist(x, y, C.first, C.second),
                   dist(x, y, D.first, D.second));
    }
    else
    {
        print_dict(dist(x, y, B.first, B.second),
                   dist(x, y, B.first, B.second),
                   dist(x, y, C.first, C.second),
                   dist(x, y, A.first, A.second));
    }
}

int main()
{
    double x ,y;

    cout << "Enter x: "; cin >> x;
    cout << "Enter y: "; cin >> y;

    // а подточка
    pair<double, double> A = {0, 0};
    pair<double, double> B = {1, 0};
    pair<double, double> C = {1, 1};
    pair<double, double> D = {0, 1};

    calc_distances(x, y, A, B, C, D);

    cout << "For the second square: " << endl;
    // б подточка
    A = {-1, -1};
    B = {1, -1};
    C = {1, 1};
    D = {-1, 1};

    calc_distances(x, y, A, B, C, D);
}