#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, to;
    cout << "Enter the array length: "; cin >> n;
    double arr[n];

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];

        string str_n = to_string(arr[i]);
        arr[i] = stod(str_n[0] + str_n);
    }

    for (int j = 0; j <= n / 2; ++j) {
        double *left = &arr[j];
        double *right = &arr[n - 1 - j];
        double swap;

        swap = *left;
        *left = *right;
        *right = swap;
    }

    for (int k = 0; k < n; ++k) {
        cout << arr[k] << " ";
    }

}