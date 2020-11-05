#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name, state, study;
    int year, term;

    cout << "Hello! What is your name?"; getline(cin, name);
    cout << "Hi, " << name << ". Nice to meet you. How are you?"; getline(cin, state);
    cout << "Do you like to study informatics in NBU?"; getline(cin, study);
    cout << "Which year are you?"; cin >> year;
    cout << "Which term you are in?"; cin >> term;

    cout << "My name is " << name << endl;
    cout << "I am feeling " << state << endl;
    cout << "I " << study << " like to study informatics in NBU" << endl;
    cout << "I am " << year << " year" << endl;
    cout << "I am " << term << " term" << endl;
    cout << "Bye!";
}