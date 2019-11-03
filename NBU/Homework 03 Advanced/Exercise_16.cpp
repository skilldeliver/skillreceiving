#include <iostream>
#include <cmath>

using namespace std;

double det(double m[3][3])
{
// finds the determinant of 3x3 matrix
return (m[0][0] * m[1][1] * m[2][2]) +
       (m[0][1] * m[1][2] * m[2][0]) +
       (m[0][2] * m[1][0] * m[2][1]) -
       (m[2][0] * m[1][1] * m[0][2]) -
       (m[2][1] * m[1][2] * m[0][0]) -
       (m[2][2] * m[1][0] * m[0][1]);
}

int main()
{
double a1, b1, c1, a2, b2, c2, a3, b3, c3, d1, d2, d3;

cout << "Enter a1: "; cin >> a1;
cout << "Enter b1: "; cin >> b1;
cout << "Enter c1: "; cin >> c1;
cout << "Enter a2: "; cin >> a2;
cout << "Enter b2: "; cin >> b2;
cout << "Enter c2: "; cin >> c2;
cout << "Enter a3: "; cin >> a3;
cout << "Enter b3: "; cin >> b3;
cout << "Enter c3: "; cin >> c3;
cout << "Enter d1: "; cin >> d1;
cout << "Enter d2: "; cin >> d2;
cout << "Enter d3: "; cin >> d3;

double D[3][3] = {
        {a1, b1, c1},
        {a2, b2, c2},
        {a3, b3, c3}
};

double Dx[3][3] = {
        {d1, b1, c1},
        {d2, b2, c2},
        {d3, b3, c3}
};

double Dy[3][3] = {
        {a1, d1, c1},
        {a2, d2, c2},
        {a3, d3, c3}
};

double Dz[3][3] = {
        {a1, b1, d1},
        {a2, b2, d2},
        {a3, b3, d3}
};

if (det(D) != 0)
{
    cout << "x is: " << det(Dx) / det(D) << endl;
    cout << "y is: " << det(Dy) / det(D) << endl;
    cout << "z is: " << det(Dz) / det(D)  << endl;
}
else
    {
    cout << "No solutions";
    }
}