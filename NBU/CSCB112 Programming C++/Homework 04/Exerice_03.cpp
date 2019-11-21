#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    string s = to_string(n);
    string new_s = "";

    for (int i = (int)s.size() - 1; i >= 0; --i) {
        new_s += s[i];
    }
    cout << new_s << endl;
    return 0;
}