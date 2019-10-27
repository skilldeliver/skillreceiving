#include <iostream>
using namespace std;


// ВАЖНА БЕЛЕЖКА
// КОДЪТ РАБОТИ САМО ЗА ПРАВИЛЕН ЧЕТИРИЪГЪЛНИК

int main()
{
    int x, x1, x2, x3, x4, y, y1, y2, y3, y4;
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

    cout << "Enter triangle D x: ";
    cin >> x4;

    cout << "Enter triangle D y: ";
    cin >> y4;

    if (x > x1 and x < x2 and y > y1 and y < y4)
        cout << "The point is in the rectangle";
    else
        cout << "The point is outside of the rectangle";
}