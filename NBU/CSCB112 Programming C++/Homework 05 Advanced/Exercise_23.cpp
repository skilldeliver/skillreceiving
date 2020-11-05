#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter the length of the arrays"; cin >> n;
    int arr1[n];
    int arr2[n];

    for (int i = 0; i < n; ++i) {
        cout << "Enter the element for the first array: "; cin >> arr1[i];
        cout << "Enter the element for the second array: "; cin >> arr2[i];

        if (arr1[i] != arr2[i])
        {
            cout << "They are different" << endl;
            return 0;
        }
    }
    cout << "They are equal" << endl;
}