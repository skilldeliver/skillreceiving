#include <cstdlib>
#include <iostream>
#include <ctime>

double get_rand_num(double min, double max)
{
    // функция връща случайно число в диапазона [min, max]
    return min + ((double)rand() / RAND_MAX) * (max - min);
}

int main()
{
    std::srand(std::time(nullptr)); // използване на времето за сийдване на генератора
    int _ = std::rand(); // първото число не е truly random

    // деклариране на променливите
    double input_num, min, max, guess;

    std::cout << "Enter minimal value for the random number: ";
    std::cin >> min;

    std::cout << "Enter maximum value for the random number: ";
    std::cin >> max;

    // генериране на случайното число и закръгляне до втори знак
    double rand_num  = get_rand_num(min, max);
    rand_num = (int)(rand_num * 100.0) / 100.0;

    // Откоментирайте този ред, за да видите числото
    // std::cout << "The random number is: " << rand_num << "\n";

    // кондиция за цикъла и брояч на опити
    bool guessed = false;
    int counter = 0;

    while (not guessed)
    {
        // взимане на число от потребител и закръгляне до втори знак
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        guess = (int)(guess * 100.0) / 100.0;

        // добавяне на опит
        counter++;

        // логиката за познаване и насочването
        if (guess == rand_num) {
            std::cout << "Congrats! U guessed the number at the " << counter << " try!";
            guessed = true;
        }
        else if (guess > rand_num)
            std::cout << "Try lower!\n";
        else
            std::cout << "Try higher!\n";

    }
}