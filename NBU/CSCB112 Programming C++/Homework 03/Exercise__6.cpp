#include <iostream>
#include <time.h>
#include <random>
#include <string>

using namespace std;


int main()
{
    double random_n, min, max;
    srand(time(NULL));
    int _ = rand(); // първото число не е truly random

    cout << "Enter the minimum: "; cin >> min;
    cout << "Enter the maximum: "; cin >> max;

    random_n = min + ((double)rand() / RAND_MAX) * (max - min);
    cout << "Result: " << random_n << endl;
}