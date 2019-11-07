#include <iostream>
#include <string>

using namespace std;

int main()
{
    int count_0 = 0; int count_1 = 0;
    int count_2 = 0; int count_3 = 0;
    int count_4 = 0; int count_5 = 0;
    int count_6 = 0; int count_7 = 0;
    int count_8 = 0; int count_9 = 0;


    int n;
    cin >> n;

    string s = to_string(n);

    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '0') count_0++;
        else if (s[i] == '1') count_1++;
        else if (s[i] == '2') count_2++;
        else if (s[i] == '3') count_3++;
        else if (s[i] == '4') count_4++;
        else if (s[i] == '5') count_5++;
        else if (s[i] == '6') count_6++;
        else if (s[i] == '7') count_7++;
        else if (s[i] == '8') count_8++;
        else if (s[i] == '9') count_9++;
    }

    cout << "0/" << count_0 << ", "
         << "1/" << count_1 << ", "
         << "2/" << count_2 << ", "
         << "3/" << count_3 << ", "
         << "4/" << count_4 << ", "
         << "5/" << count_5 << ", "
         << "6/" << count_6 << ", "
         << "7/" << count_7 << ", "
         << "8/" << count_8 << ", "
         << "9/" << count_9 << endl;
}