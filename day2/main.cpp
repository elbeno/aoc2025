#include <charconv>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

auto num_digits(auto i) { return std::to_string(i).size(); }

auto concat_digits(auto i, auto n) {
  auto s = std::string{};
  while (n--) {
    s += std::to_string(i);
  }
  std::uint64_t ret{};
  std::from_chars(s.data(), s.data() + s.size(), ret);
  return ret;
}

auto read_input() {
  auto f = std::ifstream("input");
  auto input = std::vector<std::pair<std::uint64_t, std::uint64_t>>{};

  for (std::string line{}; std::getline(f, line, ',');) {
    auto i = line.find('-');
    if (i != std::string::npos) {
      std::uint64_t start{};
      std::from_chars(line.data(), line.data() + i, start);
      std::uint64_t end{};
      std::from_chars(line.data() + i + 1, line.data() + line.size(), end);

      while (num_digits(start) != num_digits(end)) {
        auto e = static_cast<std::uint64_t>(
            std::pow(10.0f, std::floor(std::log10(end))));
        input.push_back({e, end});
        end = e - 1;
      }
      input.push_back({start, end});
    }
  }
  return input;
}

auto main() -> int {
  auto input = read_input();

  auto star1 = std::uint64_t{};
  for (auto const &p : input) {
    if (num_digits(p.first) % 2 == 0) {
      auto n = num_digits(p.first) / 2;
      auto i = static_cast<std::uint64_t>(std::pow(10.0f, n - 1));
      while (concat_digits(i, 2) < p.first) {
        ++i;
      }
      while (concat_digits(i, 2) <= p.second) {
        auto n = concat_digits(i, 2);
        star1 += n;
        ++i;
      }
    }
  }
  std::cout << star1 << '\n';

  std::unordered_set<std::uint64_t> candidates{};
  for (auto const &p : input) {
    auto k = num_digits(p.first);
    for (auto x = 1; x <= k / 2; ++x) {
      if (k % x == 0) {
        auto i = static_cast<std::uint64_t>(std::pow(10.0f, x - 1));
        auto n = k / x;
        while (concat_digits(i, n) < p.first) {
          ++i;
        }
        while (concat_digits(i, n) <= p.second) {
          auto cand = concat_digits(i, n);
          candidates.insert(cand);
          ++i;
        }
      }
    }
  }
  auto star2 = std::reduce(std::cbegin(candidates), std::cend(candidates),
                           std::uint64_t{}, std::plus{});
  std::cout << star2 << '\n';
}
