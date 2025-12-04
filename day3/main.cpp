#include <algorithm>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <vector>

auto read_input() {
  auto f = std::ifstream("input");
  auto input = std::vector<std::string>{};
  for (std::string line{}; std::getline(f, line);) {
    input.push_back(line);
  }
  return input;
}

template <int N>
auto largest_joltage = [](const std::string &s) {
  auto begin = std::cbegin(s);
  auto end = std::prev(std::cend(s), N - 1);

  std::int64_t r = 0;
  for (auto n = 0; n < N; ++n) {
    auto i = std::max_element(begin, end);
    r *= 10;
    r += (*i - '0');
    begin = std::next(i);
    ++end;
  }
  return r;
};

auto main() -> int {
  auto input = read_input();

  auto star1 =
      std::transform_reduce(std::cbegin(input), std::cend(input),
                            std::int64_t{}, std::plus{}, largest_joltage<2>);
  std::cout << star1 << '\n';
  auto star2 =
      std::transform_reduce(std::cbegin(input), std::cend(input),
                            std::int64_t{}, std::plus{}, largest_joltage<12>);
  std::cout << star2 << '\n';
}
