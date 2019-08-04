#include <vector>
#include <algorithm>

int findOdd(const std::vector<int>& numbers){
  for (auto &x : numbers)
  {
      if (std::count(numbers.begin(), numbers.end(), x) % 2 != 0) return x;
  }
}