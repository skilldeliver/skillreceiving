#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, sum;
    cout << "Enter the length of the array: "; cin >> n;
    int arr[n];

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        sum += arr[i];
    }

    for (int j = 0; j < n; ++j) {
        if (arr[j] > sum / (double)n) cout << arr[j] << " ";
    }
}