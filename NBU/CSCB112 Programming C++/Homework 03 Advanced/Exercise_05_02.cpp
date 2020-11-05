#include <iostream>
#include <string>

using namespace std;

int main()
{
int month;

cout << "Enter the month: "; cin >> month;

switch (month)
{
    case 1:
        cout << "31, January" << endl;
        break;
    case 2:
        cout << "28, February" << endl;
        break;
    case 3:
        cout << "31, March" << endl;
        break;
    case 4:
        cout << "30, April" << endl;
        break;
    case 5:
        cout << "31, May" << endl;
        break;
    case 6:
        cout << "30, June" << endl;
        break;
    case 7:
        cout << "31, July" << endl;
        break;
    case 8:
        cout << "31, August" << endl;
        break;
    case 9:
        cout << "30, September" << endl;
        break;
    case 10:
        cout << "31, October" << endl;
        break;
    case 11:
        cout << "30, November" << endl;
        break;
    case 12:
        cout << "31, December" << endl;
        break;
    default:
        cout << "Invalid month" << endl;
}
}