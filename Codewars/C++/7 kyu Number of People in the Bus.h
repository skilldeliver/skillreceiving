#include <utility>
#include <vector>

unsigned int number(const std::vector<std::pair<int, int>>& busStops){
    unsigned int number_of_people = 0;

    for (int i = 0; i < busStops.size(); ++i) {
        number_of_people += (busStops[i].first - busStops[i].second);
    }
    return number_of_people;
}