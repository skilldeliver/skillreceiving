#include <cmath>

class Tortoise
{
public:
    static std::vector<int> race(int v1, int v2, int g)
    {
        std::vector<int> ans(3);
        if (v1 >= v2)
        {
            ans[0] = -1;
            ans[1] = -1;
            ans[2] = -1;
        }
        else
        {
            int time = g * 3600 / (v2 - v1);
            int hours = time / 3600;
            int minutes = (time % 3600) / 60;
            int seconds = time % 60;


            ans[0] = hours;
            ans[1] = minutes;
            ans[2] = seconds;
        }
        return ans;
    }



};