#include <iostream>

using namespace std;

int main()
{
double n, m, p, q, a;
cout << "Enter n: "; cin >> n;
cout << "Enter m: "; cin >> m;
cout << "Enter p: "; cin >> p;
cout << "Enter q: "; cin >> q;
cout << "Enter a: "; cin >> a;

if ((((n + m) + p) + q) == a or
(((n + m) + p) - q) == a or
(((n + m) + p) * q) == a or
(((n + m) + p) / q) == a or
(((n + m) - p) + q) == a or
(((n + m) - p) - q) == a or
(((n + m) - p) * q) == a or
(((n + m) - p) / q) == a or
(((n + m) * p) + q) == a or
(((n + m) * p) - q) == a or
(((n + m) * p) * q) == a or
(((n + m) * p) / q) == a or
(((n + m) / p) + q) == a or
(((n + m) / p) - q) == a or
(((n + m) / p) * q) == a or
(((n + m) / p) / q) == a or
(((n - m) + p) + q) == a or
(((n - m) + p) - q) == a or
(((n - m) + p) * q) == a or
(((n - m) + p) / q) == a or
(((n - m) - p) + q) == a or
(((n - m) - p) - q) == a or
(((n - m) - p) * q) == a or
(((n - m) - p) / q) == a or
(((n - m) * p) + q) == a or
(((n - m) * p) - q) == a or
(((n - m) * p) * q) == a or
(((n - m) * p) / q) == a or
(((n - m) / p) + q) == a or
(((n - m) / p) - q) == a or
(((n - m) / p) * q) == a or
(((n - m) / p) / q) == a or
(((n * m) + p) + q) == a or
(((n * m) + p) - q) == a or
(((n * m) + p) * q) == a or
(((n * m) + p) / q) == a or
(((n * m) - p) + q) == a or
(((n * m) - p) - q) == a or
(((n * m) - p) * q) == a or
(((n * m) - p) / q) == a or
(((n * m) * p) + q) == a or
(((n * m) * p) - q) == a or
(((n * m) * p) * q) == a or
(((n * m) * p) / q) == a or
(((n * m) / p) + q) == a or
(((n * m) / p) - q) == a or
(((n * m) / p) * q) == a or
(((n * m) / p) / q) == a or
(((n / m) + p) + q) == a or
(((n / m) + p) - q) == a or
(((n / m) + p) * q) == a or
(((n / m) + p) / q) == a or
(((n / m) - p) + q) == a or
(((n / m) - p) - q) == a or
(((n / m) - p) * q) == a or
(((n / m) - p) / q) == a or
(((n / m) * p) + q) == a or
(((n / m) * p) - q) == a or
(((n / m) * p) * q) == a or
(((n / m) * p) / q) == a or
(((n / m) / p) + q) == a or
(((n / m) / p) - q) == a or
(((n / m) / p) * q) == a or
(((n / m) / p) / q) == a)
{
    cout << "It exists";
}
else
    {
        cout << "It doesn't exists";
    }
}