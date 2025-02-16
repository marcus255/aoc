#include "../inc/tasklist.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
#include <tuple>

namespace Task_2024_01 {

Task::Task()
    : AocTask{"2024_01", "11", "31"} {
}

auto getVectors(const std::vector<std::string>& input) {
    std::vector<int> left;
    std::vector<int> right;

    for (auto line : input) {
        // line has format "123   456"
        size_t pos = line.find("   ");
        if (pos != std::string::npos) {
            left.push_back(std::stoi(line.substr(0, pos)));
            right.push_back(std::stoi(line.substr(pos + 3)));
        } else {
            throw std::runtime_error("Invalid input format");
        }
    }
    return std::make_tuple(left, right);
}

std::string Task::partOneSolution(const std::vector<std::string>& input) {
    auto [left, right] = getVectors(input);

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());
    std::vector<int> distances(left.size());
    std::transform(left.begin(), left.end(), right.begin(), distances.begin(), [](int l, int r) {
        return std::abs(l - r);
    });

    return std::to_string(std::accumulate(distances.begin(), distances.end(), 0));
}

std::string Task::partTwoSolution(const std::vector<std::string>& input) {
    auto vectors = getVectors(input);
    auto& [left, right] = vectors;

    std::vector<int> scores;
    for_each(left.begin(), left.end(), [&](int l) {
        // To make the code complient with C++17, we cannot capture unpacked tuple
        auto& [left, right] = vectors;
        scores.push_back(l * std::count(right.begin(), right.end(), l));
    });

    return std::to_string(std::accumulate(scores.begin(), scores.end(), 0));
}
}
