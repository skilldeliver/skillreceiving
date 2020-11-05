#include <iostream>

using namespace std;

int main()
{
    int k;
    cout << "Enter k: "; cin >> k;

    int arr[2 * k + 1];

    for (int i = 0; i < 2 * k + 1; ++i) {
        cin >> arr[i];
        if (arr[i] == k - 1)
        {
            cout << arr[i];
            return 0;
        }
    }
}