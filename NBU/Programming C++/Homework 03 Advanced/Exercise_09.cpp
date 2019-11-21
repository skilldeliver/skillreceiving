#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b;

    cout << "Enter a: "; cin >> a;
    cout << "Enter b: "; cin >> b;

    cout << min(a, b) * 3 << " " << max(a, b) / 5 << endl;
}