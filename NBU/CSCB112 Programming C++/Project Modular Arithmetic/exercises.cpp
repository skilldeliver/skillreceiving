//
// Created by Skill on 02-Jan-20.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#include "exercises.h"

using namespace std;

// helper functions
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int reciprocal(int a, int n){
    if (gcd(n, a) != 1) {
        return -1;
    }
    int count = 1;

    while (a % n != 1)
    {
        a += a / count;
        count++;
    }
    return count;
}

int* fill_array(int n)
{
    int* array = new int[n];
    cout << "Zn elements: ";
    for (int i = 0; i < n; ++i) {
        array[i] = i;
        cout << i << " ";
    }
    cout << endl;
    return array;
} // 1

int add(int n, int a, int b)
{
    if (!(0 <= a and a <= n) or !(0 <= b and b <= n)) {
        cout << "a and b should be numbers from Zn elements." << endl;;
        return -1;
    }

    return (a + b) % n;
} // 2

int subtract(int n, int a, int b)
{
    if (!(0 <= a and a <= n) or !(0 <= b and b <= n)) {
        cout << "a and b should be numbers from Zn elements." << endl;
        return -1;
    }
    int r = (a - b) % n;
    return r < 0 ? r + n : r;
} // 3

int multiply(int n, int a, int b)
{
    if (!(0 <= a and a <= n) or !(0 <= b and b <= n)) {
        cout << "a and b should be numbers from Zn elements." << endl;;
        return -1;
    }
    return (a * b) % 7;
} // 4

int** fill_reciprocal(int n)
{
    int** array;
    array = new int*[n];
    cout << "Reciprocal elements in Zn: (-1 means that there is None)" << endl;

    for (int i = 0; i < n; ++i) {
        array[i]  = new int[2];

        array[i][0] = i;
        array[i][1] = reciprocal(i, n);

        cout << array[i][0] << " : " << array[i][1] << endl;
    }

    return array;
} // 5

int find_reciprocal(int** reciprocals, int n, int a)
{
    for (int i = 0; i < n; ++i) {
        if (reciprocals[i][0] == a)
            return reciprocals[i][1];
    }
    return -1;
} // 6

int find_reciprocal_bezu(int a, int b)
{
    if (!(b >= 0 and b < a)) {
        cout << "Should be in the range of n." << endl;
        return -1;
    }

    int safe_a = a;
    int y0 = 1;
    int y1 = 0;

    while (a != 0) {
        div_t result =  div(b, a);

        int q = result.quot;
        b = a;
        a = result.rem;

        int temp = y1;
        y1 = y0 - q*y1;
        y0 = temp;
    }

    if (b  != 1) return -1;
    return y0 < 0 ? y0 + safe_a : y0;
} // 7

int divide(int n, int a, int b)
{
    int reciprocal = find_reciprocal_bezu(n, b);
    return reciprocal == -1 ? -1 : multiply(n, a, reciprocal);
}  // 8

int fast_exponent(int n, int base, int exponent)
{
    int result = base;
    int e = 1;

    while (result != 1)
    {
        result = (base * result) % n;
        e++;
    }
    return (int) pow(base, exponent%e) % n;
} // 9

int fast_exponent_2(int n, int base, int exponent)
{
    int value = base % n;
    int result = 1;

    while (exponent != 0) {
        if (exponent % 2 == 1)
            result *= value;

        value = (int) pow(value, 2) % n;
        exponent /= 2;
    }
    return result % n;
} // 10

bool is_primal_root(int n, int g)
{
    vector<int> primes;

    for (int i = 0; i < n; ++i) {
        if (gcd(n, i) == 1) primes.push_back(i);
    }
    vector<int> values;

    for (int j = 1; j <= primes.size(); j++)
    {
        values.push_back((int)(pow(g, j) + 0.5)  % n);
    }

    sort(values.begin(), values.end());
    for (int k = 0; k < primes.size(); ++k) {
        if (primes[k] != values[k]) return false;
    }
    return true;
} // 11

void all_primes(int n)
{
    int len = 0;
    for (int i = 0; i < n; ++i) {
        if (is_primal_root(n, i)) len++;
    }
    int* primes = new int[len];
    len = 0;
    cout << "All primal roots in Zn: ";
    for (int j = 0; j < n; ++j){
        if (is_primal_root(n, j)){
            cout << j << " ";
            primes[len] = j;
            len++;
        }
    }
    cout << endl;
} // 12

int dlog(int n, int base, int el)
{
    if (not is_primal_root(n, base)) return -1;
    if (el == 1) return 0;

    for (int i = 0; i < n; ++i) {
        if (gcd(n, i) == 1)
        {
            if ((int)(pow(base, i) + 0.5) % n == el) return i;
        }
    }
    return -1;
} // 13

bool is_remainding_ring(int n)
{
    if (n <= 1)
        return false;

    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;

    return true;
} // 14