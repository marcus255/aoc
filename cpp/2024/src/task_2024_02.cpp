#include "../inc/tasklist.h"
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

namespace Day_2024_02 {

Task::Task()
    : AocTask{"2024_02", "2", "4"} {
}

auto convertStringToVector(const std::string& input) {
    std::vector<int> result;
    std::istringstream iss(input);
    int number;
    while (iss >> number) {
        result.push_back(number);
    }
    return result;
}

auto convertInputToVector(const std::vector<std::string>& input) {
    std::vector<std::vector<int>> result;
    for (auto line : input) {
        result.push_back(convertStringToVector(line));
    }
    return result;
}

bool isReportSafe(const std::vector<int>& numbers) {
    bool sortedAsc = std::is_sorted(numbers.begin(), numbers.end(), std::less_equal<int>());
    bool sortedDesc = std::is_sorted(numbers.begin(), numbers.end(), std::greater_equal<int>());
    auto it = std::adjacent_find(numbers.begin(), numbers.end(), [](int a, int b) {
        return abs(a - b) < 1 || abs(a - b) > 3;
    });
    bool diffOk = it == numbers.end();
    // TODO: Allow verbose output but only for test mode, not for task mode
    // std::cout << line << " sorted: " << sortedAsc << sortedDesc << " adj: " << diffOk << std::endl;

    return diffOk && (static_cast<int>(sortedAsc) + static_cast<int>(sortedDesc) == 1);
}

std::string Task::partOneSolution(const std::vector<std::string>& input) {
    auto allNumbers = convertInputToVector(input);
    int safe = 0;
    for (auto numbers : allNumbers) {
        if (isReportSafe(numbers)) {
            safe++;
        }
    }

    return std::to_string(safe);
}

std::string Task::partTwoSolution(const std::vector<std::string>& input) {
    auto allNumbers = convertInputToVector(input);
    int safe = 0;
    for (auto numbers : allNumbers) {
        for (size_t i = 0; i < numbers.size(); i++) {
            std::vector<int> newNumbers = numbers;
            newNumbers.erase(newNumbers.begin() + i);
            if (isReportSafe(newNumbers)) {
                safe++;
                break;
            }
        }
    }

    return std::to_string(safe);
}
}
