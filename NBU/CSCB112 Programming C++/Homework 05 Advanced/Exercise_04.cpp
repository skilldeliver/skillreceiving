#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, count = 0, len = 0, max_len = 0;
    cout << "Enter the array length: "; cin >> n;
    int arr[n];

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];

        if (i != 0)
        {
            if (arr[i] == arr[i - 1]) len++;
            if (arr[i] != arr[i - 1] or (arr[i] == arr[i - 1] and i == n - 1))
                {
                len++;
                if (len > max_len) max_len = len;
                if (len != 1) count++;
                len = 0;
                }
        }
    }

    cout << "Largest count of equal items: " << max_len << endl;
    cout << "Count of equal items groups: " << count << endl;
}