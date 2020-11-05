# include <string>
# include <vector>

std::string disemvowel(std::string str)
{
    std::vector<char> vowels = {'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'};
    std::string final;

    for (int i = 0; i < str.size(); ++i) {
        bool is_in = false;
        for (int j = 0; j < vowels.size(); ++j) {
            if (str[i] == vowels[j]) {
                is_in = true;
                break;
            }
        }
        if (not is_in)
            final += str[i];
    }
    return final;

}