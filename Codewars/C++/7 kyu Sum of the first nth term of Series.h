#include <cmath>
#include <string>

std::string to_string_with_precision(const double a_value, const int n = 2)
{
    std::ostringstream out;
    out.precision(n);
    out << std::fixed << a_value;
    return out.str();
}

std::string seriesSum(int n)
{
    double denominator = 4;
    double num = 0;
    for (int i = 1; i < n; ++i, denominator+=3) {
        num += (1 / denominator);
    }

    if (n == 0)
        return "0.00";
    num += 1;

    double rounded = std::floor((num * 100) + .5) / 100;
    return to_string_with_precision(rounded);
}

