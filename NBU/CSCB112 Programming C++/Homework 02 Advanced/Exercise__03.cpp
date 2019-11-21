#include <iostream>

using namespace std;

int main()
{
    int arr[] = {1, 2, 4, 6, 3, 8, 7};
    int xor_1 = arr[0];
    int xor_2 = 1;

    for (int i = 0; i < sizeof(arr)/sizeof(*arr); i++)
        xor_1 ^= arr[i];

    for (int i = 1; i <= sizeof(arr)/sizeof(*arr) + 1; i++)
        xor_2 = xor_2 ^ i;

    cout << (xor_1 ^ xor_2);
} 