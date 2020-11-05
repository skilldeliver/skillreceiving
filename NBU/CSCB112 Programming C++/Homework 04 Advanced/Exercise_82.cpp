#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int main()
{
    int n1; int n2;
    int i; int j;

    cout << "Enter n1: "; cin >> n1;
    cout << "Enter n2: "; cin >> n2;
    cout << "Enter i: "; cin >> i;
    cout << "Enter j: "; cin >> j;

    string binary_1 = std::bitset<32>(n1).to_string();
    string binary_2 = std::bitset<32>(n2).to_string();

    if (binary_1[abs(i-32)] == binary_2[abs(j-32)])
        cout << "They match";
    else
        cout << "They don't match";
    return 0;
}