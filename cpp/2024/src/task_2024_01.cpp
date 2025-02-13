#include "../inc/task_2024_01.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>

Task_2024_01::Task_2024_01()
    : AocTask{"2024_01", "11", "31"} {
}

std::string solution1(std::vector<std::string> input) {
    std::vector<int> left;
    std::vector<int> right;

    for (auto line : input) {
        // line has a format "123   456"
        size_t pos = line.find("   ");
        if (pos != std::string::npos) {
            left.push_back(std::stoi(line.substr(0, pos)));
            right.push_back(std::stoi(line.substr(pos + 3)));
        } else {
            throw std::runtime_error("Invalid input format");
        }
    }
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());
    std::vector<int> distances(left.size());
    std::transform(left.begin(), left.end(), right.begin(), distances.begin(), [](int l, int r) {
        return std::abs(l - r);
    });
    int sum = std::accumulate(distances.begin(), distances.end(), 0);

    return std::to_string(sum);
}

// TODO: rename virtual methots to solution1 and solution2, run them for test and task input
std::string Task_2024_01::part1Test() {

    // TODO: move to AocTask and show contitionally based on verbose flag
    // std::cout << "test input:" << std::endl;
    // for_each(test_input.begin(), test_input.end(), [](std::string line) {
    //     std::cout << line << std::endl;
    // });

    return solution1(test_input);
}

std::string Task_2024_01::part1() {
    return solution1(task_input);
}

std::string solution2(std::vector<std::string> input) {
    // TODO: commonalize with solution1
    std::vector<int> left;
    std::vector<int> right;

    for (auto line : input) {
        // line has a format "123   456"
        size_t pos = line.find("   ");
        if (pos != std::string::npos) {
            left.push_back(std::stoi(line.substr(0, pos)));
            right.push_back(std::stoi(line.substr(pos + 3)));
        } else {
            throw std::runtime_error("Invalid input format");
        }
    }

    std::vector<int> scores;
    for_each(left.begin(), left.end(), [&](int l) {
        scores.push_back(l * std::count(right.begin(), right.end(), l));
    });

    return std::to_string(std::accumulate(scores.begin(), scores.end(), 0));
}

std::string Task_2024_01::part2Test() {
    // std::cout << "test input:" << std::endl;
    // for_each(test_input.begin(), test_input.end(), [](std::string line) {
    //     std::cout << line << std::endl;
    // });

    return solution2(test_input);
}


std::string Task_2024_01::part2() {
    return solution2(task_input);
}