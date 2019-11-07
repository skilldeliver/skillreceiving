#include <iostream>

using namespace std;

double calc(double i, int to)
{
    if (i == to)
        return 1.0 / 111;
    return 1 / (i + calc(i+2, to));

}

int main()
{
    cout << 1/calc(1.0, 111);
}