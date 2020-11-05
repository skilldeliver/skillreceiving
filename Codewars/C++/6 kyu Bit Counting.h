  unsigned int countBits(unsigned long long n){
    int sum = 0;
    std::string binary = std::bitset<8>(n).to_string();

    for (int i = 0; i < binary.size(); ++i) {
        if (binary[i] == '1')
          sum += 1;
    }
    return sum;
  }