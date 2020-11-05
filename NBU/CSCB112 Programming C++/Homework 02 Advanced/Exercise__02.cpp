#include <iostream>

using namespace std;

int main()
{
    int odd;
    int arr[] = {10, 20, 10, 30, 10, 10, 20};

    for (int i = 0; i < sizeof(arr)/sizeof(*arr); i++)
        odd ^= arr[i];
    cout << odd;
} 