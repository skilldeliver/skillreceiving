#include <iostream>
#include <chrono>

#include "exercises.h"

using namespace std;

int main() {
    int n = -1;
    int a, b;
    int* Zn;
    int ** reciprocal_Zn;
    int e = 1;

    while (e != 0){
        cout << "Enter exercise number: "; cin >> e;

        if (not(e >= 0 and e <= 14) ) continue;

        if (n == -1 and not(e == 9 or e == 10 or e == 1)) {
            cout << "Enter n for Zn first (Exercise 1)!" << endl;
            continue;
        }

        if (e == 1)
        {
            cout << "Enter n: "; cin >> n;
            Zn = fill_array(n);
        }
        else if(e == 2)
        {
            cout << "Enter operand a: "; cin >> a;
            cout << "Enter operand b: "; cin >> b;
            int result =  add(n, a, b);

            if (result != -1) cout << "The addition of a and b in Zn is: "; cout << result << endl;
        }
        else if(e == 3)
        {
                cout << "Enter operand a: "; cin >> a;
                cout << "Enter operand b: "; cin >> b;
                int result = subtract(n, a, b);
                if (result != -1)  cout << "The subtraction of a and b in Zn is: " << result << endl;
        }
        else if(e == 4)
        {
                cout << "Enter operand a: "; cin >> a;
                cout << "Enter operand b: "; cin >> b;
                int result = multiply(n, a, b);
                if (result != -1) cout << "The product of a and b in Zn: is" << result << endl;
        }
        else if(e == 5)
        {
                reciprocal_Zn = fill_reciprocal(n);
        }
        else if(e == 6)
        {
            if (reciprocal_Zn == NULL) cout << "Recirpocal of Zn is not initilaized." << endl;
            else {
                cout << "Enter element from Zn: ";
                cin >> a;
                auto start = chrono::steady_clock::now();
                int reciprocal = find_reciprocal(reciprocal_Zn, n, a);
                auto end = chrono::steady_clock::now();
                auto diff = end - start;
                cout << "The reciprocal of " << a << " << in Zn is: " << reciprocal << endl;
                cout << "Time execution: " << chrono::duration <double, nano> (diff).count() << endl;
            }
        }
        else if(e == 7)
        {
            cout << "Enter element from Zn: ";
            cin >> a;
            auto start = chrono::steady_clock::now();
            int reciprocal = find_reciprocal_bezu(n, a);
            auto end = chrono::steady_clock::now();
            auto diff = end - start;
            cout << "The reciprocal of " << a << "  in Zn is: " << reciprocal << endl;
            cout << "Time execution: " << chrono::duration <double, nano> (diff).count() << endl;
        }
        else if(e == 8)
        {
            cout << "Enter operand a: "; cin >> a;
            cout << "Enter operand b: "; cin >> b;
            int result = divide(n, a, b);
            if (result != -1) cout << "The division of a and b in Zn is:" << result << endl;
            else cout << "Not possible." << endl;
        }
        else if(e == 9)
        {
            int n_Zn, base, exponent;
            cout << "Enter n of Zn: "; cin >> n_Zn;
            cout << "Enter base: "; cin >> base;
            cout << "Enter exponent: "; cin >> exponent;
            auto start = chrono::steady_clock::now();
            cout << "The result is " << fast_exponent(n_Zn, base, exponent) << endl;
            auto end = chrono::steady_clock::now();
            auto diff = end - start;
            cout << "Time execution: " << chrono::duration <double, nano> (diff).count() << endl;
        }
        else if(e == 10)
        {
            int n_Zn, base, exponent;
            cout << "Enter n of Zn: "; cin >> n_Zn;
            cout << "Enter base: "; cin >> base;
            cout << "Enter exponent: "; cin >> exponent;
            auto start = chrono::steady_clock::now();
            cout << "The result is " << fast_exponent_2(n_Zn, base, exponent) << endl;
            auto end = chrono::steady_clock::now();
            auto diff = end - start;
            cout << "Time execution: " << chrono::duration <double, nano> (diff).count() << endl;
        }
        else if(e == 11)
        {
            cout << "Enter a: "; cin >> a;

            if (is_primal_root(n, a)) cout << a << " is primal root in Zn." << endl;
            else cout << a << " is not a primal root in Zn." << endl;
        }
        else if(e == 12)
        {
            all_primes(n);
        }
        else if(e == 13)
        {
            int base, el;
            cout << "Enter base: "; cin >> base;
            cout << "Enter element: "; cin >> el;
            cout << "The result is " << dlog(n, base, el) << endl;
        }
        else if(e == 14)
        {
            if (is_remainding_ring(n))
            {
            cout << "Zn is Fn" << endl;
            }
            else
                {
                cout << "Zn is not Fn" << endl;
                }
        }
    }

    // delete dynamic arrays
    delete[] Zn;

    return 0;
}
