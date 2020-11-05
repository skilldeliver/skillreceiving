#include <iostream>
#include <string>

using namespace std;

string roman(int num) {
    string result;

    string letters[] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
    int nums[] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
    int i = sizeof(nums)/sizeof(*nums) - 1;

    while (num > 0) {
        int times = num / nums[i];
        num = num % nums[i];

        for (int j = 0; j < times; ++j) {
            result += letters[i];	
        }
        i--;
    }
    return result;
}

int main()
{
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << roman(n);
    return 0;
}