#include <string>
#include <iostream>

bool chessBoardCellColor(std::string cell1, std::string cell2) {
  return ((cell1[0] - 64) % 2 == 0) == ((cell1[1] - 48) % 2 == 0) == ((cell2[0] - 64) % 2 == 0) == ((cell2[1] - 48) % 2 == 0);
}