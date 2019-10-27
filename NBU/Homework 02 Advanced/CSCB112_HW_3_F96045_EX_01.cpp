#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int largest = 0, sum = 0, number, n;

    cout << "Enter the number: "; cin >> number;
    cout << "Enter n: "; cin >> n;

    if (number / n != 0) {
        cout << "The n-th digit of the number is: " << to_string(number)[n - 1] << endl;

        bool even = (int) to_string(number)[n - 1] % 2 == 0;
        int n2 = number;

        while (n2 != 0) {
            int digit = n2 % 10;
            largest = max(digit, largest);

            sum += digit;

            n2 /= 10;
        }
        cout << "The largest digit is: " << largest << endl;
        cout << "The sum of the digits is: " << sum << endl;

        if (even) cout << "The n-th digit is even." << endl;
        else cout << "The n-th digit is not even." << endl;

        if (sum % 2 == 0) cout << "The sum of the digits is even." << endl;
        else cout << "The sum of the digits is not even." << endl;

        int count = 0;
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                cout << i << " is divisor." << endl;
                count++;
            }
        }
        cout << "Total number of divisors is " << count << endl;
    }
    else
        {
        cout << "The number should be n-size!";
        }
    return 0;
}