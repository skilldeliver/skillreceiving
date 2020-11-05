#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n = 0;
    cout << "Enter an integer: "; cin >> n;
    string str_n = to_string(n);

    for (int i = 0; i < str_n.size(); ++i) {
        cout << str_n[i] << endl;
    }

}