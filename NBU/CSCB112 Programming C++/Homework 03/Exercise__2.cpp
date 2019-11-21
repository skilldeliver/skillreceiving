#include <iostream>
#include <string>
#include <iterator>
#include <map>

using namespace std;

int roman_to_int(string roman) {
    int result = 0;
    map<string, int> values {
        pair<string, int>("I", 1),
        pair<string, int>("IV", 4),
        pair<string, int>("V", 5),
        pair<string, int>("IX", 9),
        pair<string, int>("X", 10),
        pair<string, int>("XL", 40),
        pair<string, int>("L", 50),
        pair<string, int>("XC", 90),
        pair<string, int>("C", 100),
        pair<string, int>("CD", 400),
        pair<string, int>("D", 500),
        pair<string, int>("CM", 900),
        pair<string, int>("M", 1000)
                };

    for (int i = 0; i < roman.size(); ++i) {

        if (i != roman.size() - 1)
        {
            string value = string(1, roman[i]) + string(1, roman[i + 1]);
            if ( values.find(value) != values.end() )
            {
                result += values[value];
                i++;
                continue;
            }
        }
        if ( values.find(string(1, roman[i])) != values.end() )
        {
            result += values[string(1, roman[i])];
        }
    }
    return result;
}

int main()
{
    string roman_n;
    cout << "Enter number: ";
    cin >> roman_n;
    cout << roman_to_int(roman_n);
    return 0;
}