#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

auto read_input() {
  auto f = std::ifstream("input");
  auto input = std::vector<std::string>{};

  for (std::string line{}; std::getline(f, line);) {
    using namespace std::string_literals;
    input.push_back("."s + line + ".");
  }
  auto wall = std::string(input[0].size(), '.');
  input.insert(input.begin(), wall);
  input.push_back(wall);
  return input;
}

auto check(std::vector<std::string> const &v, std::size_t x, std::size_t y)
    -> bool {
  if (v[x][y] != '@') {
    return false;
  }
  auto count = 0;
  for (auto i = -1; i <= 1; ++i) {
    for (auto j = -1; j <= 1; ++j) {
      count += v[x + i][y + j] == '@';
    }
  }
  return count < 5;
}

auto mark(std::vector<std::string> const &in, std::vector<std::string> &out,
          std::size_t N, std::size_t M) -> std::uint64_t {
  std::uint64_t r = 0;
  for (auto i = std::size_t{1}; i < N - 1; ++i) {
    for (auto j = std::size_t{1}; j < M - 1; ++j) {
      if (check(in, i, j)) {
        out[i][j] = '.';
        ++r;
      }
    }
  }
  return r;
}

auto main() -> int {
  auto input = read_input();
  for (auto const &s : input) {
    std::cout << s << '\n';
  }
  std::cout << '\n';

  auto output = input;
  auto removed = mark(input, output, input.size(), input[0].size());
  for (auto const &s : output) {
    std::cout << s << '\n';
  }

  std::cout << removed << '\n';

  auto star2 = removed;
  while (removed > 0) {
    input = output;
    removed = mark(input, output, input.size(), input[0].size());
    star2 += removed;
    std::cout << removed << '\n';
  }
  std::cout << star2 << '\n';
}
