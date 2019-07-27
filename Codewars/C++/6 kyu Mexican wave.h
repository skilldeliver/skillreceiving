#include <vector>
#include <string>

std::vector<std::string> wave(std::string y){
    std::vector<std::string> waves;

    for (int i = 0; i < y.size(); ++i) {
        if (y[i] != ' ')
        {
            std::string new_string = y;
            new_string[i] = (char)(new_string[i] - 32);
            waves.push_back(new_string);
        }
    }
    return waves;
}
