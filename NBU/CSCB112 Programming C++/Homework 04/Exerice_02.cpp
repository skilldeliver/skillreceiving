#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    int sum;
    cin >> n;

    string s = to_string(n);

    for (int i = 0; i < s.size(); ++i) {
        sum += s[i] - 48;
        cout << sum << endl;
    }
    cout << sum;
    return 0;
}