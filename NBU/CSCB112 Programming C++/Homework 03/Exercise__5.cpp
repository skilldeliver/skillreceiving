#include <iostream>
#include <time.h>
#include <random>
#include <string>

using namespace std;

void print_digits(int num)
{
    string str_n = to_string(num);

    for (int i = 0; i < str_n.size(); ++i) {
        cout << str_n[i] << endl;
    }
}

int main()
{
    int random_n, min, max;
    srand(time(NULL));

    cout << "Enter the minimum: "; cin >> min;
    cout << "Enter the maximum: "; cin >> max;

    random_n = min + rand() % ((max + 1) - min);
    cout << random_n << " !" << endl;

    if (random_n >= 100){
        print_digits(random_n);
    }
}