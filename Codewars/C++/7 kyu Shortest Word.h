int find_short(std::string str)
{
    int smallest = INT_MAX;
    int len = 0;

    for (int i = 0; i < str.size(); ++i){
        if (str[i] == ' ' or i == str.size() - 1)
        {
            if (i == str.size() - 1 && str[i] != ' ')
                len++;
            if (len < smallest)
                smallest = len;
            len = 0;
        }
        else
            len += 1;

    }
    return smallest;
}