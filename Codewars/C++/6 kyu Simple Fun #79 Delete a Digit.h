#include <string>

int deleteDigit(int n)
{
    int max = INT_MIN;
    std::string str_n = std::to_string(n);

    for (int i = 0; i < str_n.size(); ++i) {
        std::string new_str = "";
        for (int j = 0; j < str_n.size() ; ++j) {
            if (i != j)
                new_str += new_str[j];
        }
        int num = std::stoi(new_str);

        if (num > max)
            max = num;
    }
    return max;
}