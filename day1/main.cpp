#include <charconv>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

auto read_input() {
  auto f = std::ifstream("input");
  auto input = std::vector<int>{};
  for (std::string line{}; std::getline(f, line);) {
    int rot{};
    std::from_chars(&line[1], line.data() + line.size(), rot);
    if (line[0] == 'L') {
      input.push_back(-rot);
    } else {
      input.push_back(rot);
    }
  }
  return input;
}

auto main() -> int {
  auto input = read_input();
  auto dialpos = 50;
  auto star1 = 0;
  auto star2 = 0;

  auto inc_1 = [&] {
    if (dialpos == 0) {
      ++star1;
    }
  };
  auto inc_2 = [&] {
    if (dialpos == 0) {
      ++star2;
    }
  };

  for (auto i : input) {
    auto inc = i > 0 ? 1 : -1;
    while (i != 0) {
      dialpos += inc;
      dialpos %= 100;
      i -= inc;
      inc_2();
    }
    inc_1();
  }
  std::cout << star1 << '\n';
  std::cout << star2 << '\n';
}
