#include <string>
#include <iostream>

std::string reverse_words(std::string str)
{
    std::string result = "";
    int start = 0;

    for (int i = 0; i < str.size(); i++) {
        if ((i == (str.size() - 1) && str[i] != ' ') or (str[i + 1] == ' ' and str[i] != ' '))
        {
            for (int j = i; j >= start; j--) {
                result += str[j];
            }
        }
        else if (str[i] == ' ')
        {
            start = i + 1;
            result += ' ';
        }

    }
    return result;
}
