static long findMissing(std::vector<long> list){
    int common_diff = list[1] - list[0];

    for (int i = 1; i < list.size(); ++i) {
        if ((list[i] - list[i - 1]) != common_diff)
        {
            return list[i] - common_diff;
        }
    }
}