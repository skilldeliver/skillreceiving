#include <string>
#include <vector>
#include <iostream>
#include <map>

class Fracts
{

public:
    static std::string convertFrac(std::vector<std::vector<unsigned long long>> &lst);
    static std::map<std::string, int> factors_of_n(unsigned long long n);
    static unsigned long long product(std::map<std::string, int>);
};

unsigned long long Fracts::product(std::map<std::string, int> factors)
{
    unsigned long long total_prod = 1;

        for (auto &x: factors){
        unsigned long long pow = (unsigned long long)std::stoi(x.first);
        for (unsigned long long i = 1; i < x.second; ++i) {
            pow *= (unsigned long long)std::stoi(x.first);
        }
        total_prod *= pow;
    }
    return total_prod;

}

std::map<std::string, int> Fracts::factors_of_n(unsigned long long n) {
    std::map<std::string, int> factors_count;
    while (n > 1) {
        for (int i = 2; i <= n; ++i) {
            if (n % i == 0) {
                n = n / i;
                auto it = factors_count.find(std::to_string(i));
                if (it != factors_count.end()) {
                    it->second++;    // increment map's value for key 'c'
                }
                    // key not found
                else {
                    factors_count.insert(std::make_pair(std::to_string(i), 1));
                }
                break;

            }

        }
    }
    return factors_count;
}

std::string Fracts::convertFrac(std::vector<std::vector<unsigned long long>> &lst) {
    std::string output = "";
    std::map<std::string, int> total;
    for (int i = 0; i < lst.size(); ++i) {
        unsigned long long denominator = lst[i][1];
        std::map<std::string, int> factors = factors_of_n(denominator);

        for (auto &x : factors) {
            if (total.find(x.first) != total.end() || x.second > total[x.first]) {
                total[x.first] = x.second;
            }
        }
    }
    unsigned long long denom = product(total);
    for (int j = 0; j < lst.size(); ++j) {
        output += "(" + std::to_string(lst[j][0] * (denom / lst[j][1])) + "," + std::to_string(denom) + ")";
    }
    return output;
}
