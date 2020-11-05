#include <vector>

class Kata
{
public:
    std::vector<int> sortArray(std::vector<int> array)
    {
        std::vector<int> odds;

        for (int i = 0; i < array.size(); ++i) {
            if (array[i] % 2 != 0)
                odds.push_back(array[i]);
        }
        sort(odds.begin(), odds.end());

        int k = 0;
        for (int j = 0; j < array.size(); ++j) {
            if (array[j] % 2 != 0)
            {
                array[j] = odds[k];
                k++;
            }
        }
        return array;
    }
};