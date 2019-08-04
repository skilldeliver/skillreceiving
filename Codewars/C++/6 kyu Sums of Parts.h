#include<vector>
#include <iostream>

std::vector<unsigned long long> partsSum(const std::vector<unsigned long long>& ls){
    std::vector<unsigned long long> parts_sum(ls.size() + 1);
    unsigned long long sum = 0;
    for (int i = ls.size() - 1; i > -1; --i) {
        parts_sum[i + 1] = sum;
        sum += ls[i];
    }
    parts_sum[0] = sum;

    return parts_sum;
}