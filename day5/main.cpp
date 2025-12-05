#include <algorithm>
#include <charconv>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <utility>
#include <vector>

auto read_input() {
  auto f = std::ifstream("input");
  auto ranges = std::vector<std::pair<std::uint64_t, std::uint64_t>>{};
  auto tests = std::vector<std::uint64_t>{};

  for (std::string line{}; std::getline(f, line);) {
    if (auto i = line.find('-'); i != std::string::npos) {
      std::uint64_t start{};
      std::from_chars(line.data(), line.data() + i, start);
      std::uint64_t end{};
      std::from_chars(line.data() + i + 1, line.data() + line.size(), end);
      ranges.push_back({start, end});
    } else if (not line.empty()) {
      std::uint64_t n{};
      std::from_chars(line.data(), line.data() + line.size(), n);
      tests.push_back(n);
    }
  }
  return std::pair{ranges, tests};
}

auto main() -> int {
  auto [ranges, tests] = read_input();

  auto in_any_range = [&ranges = ranges](auto n) -> bool {
    return std::any_of(std::cbegin(ranges), std::cend(ranges),
                       [&](auto r) { return n >= r.first and n <= r.second; });
  };

  auto star1 =
      std::count_if(std::cbegin(tests), std::cend(tests), in_any_range);
  std::cout << star1 << '\n';

  std::sort(std::begin(ranges), std::end(ranges),
            [](auto x, auto y) { return x.first < y.first; });

  auto merged_ranges = std::vector<std::pair<std::uint64_t, std::uint64_t>>{};
  for (auto [x, y] : ranges) {
    auto i = std::find_if(std::begin(merged_ranges), std::end(merged_ranges),
                          [&x = x](auto p) { return x <= p.second; });
    if (i == std::end(merged_ranges)) {
      merged_ranges.push_back(std::pair{x, y});
    } else {
      i->second = std::max(i->second, y);
    }
  }
  auto star2 = std::transform_reduce(
      std::cbegin(merged_ranges), std::cend(merged_ranges), std::uint64_t{},
      std::plus{}, [](auto p) { return p.second - p.first + 1; });
  std::cout << star2 << '\n';
}
