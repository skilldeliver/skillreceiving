#include <iostream>
#include <string>
#include <random>
#include <ctime>

using namespace std;

int random(int min, int max)
{
    static bool first = true;
    if (first)
    {
        srand( time(NULL) );
        first = false;
    }
    return min + rand() % (( max + 1 ) - min);
}

int main()
{
    int n; int hint; int count = 0;
    cout << "Enter your number: "; cin >> n;
    int low = 0; int high = 100;

    if (not(n >= low and n <= high))
    {
        cout << "The number must be in 0-100 range " << endl;
        return 0;
    }

    do {
        int guess = random(low, high);
        cout << "Computer guess: " << guess << endl;
        cout << "Enter 0 if matches, 1 if the guess is low, and -1 if the guess is high: "; cin >> hint;

        if (hint == 1) low = guess + 1;
        else if (hint == -1) high = guess - 1;
        count++;

    } while (hint != 0 and count <= 7);

    if (hint == 0) cout << "The computer guessed it at the " << count << " try" << endl;
    else cout << "The computer did not managed to guess it";
}