#include "../inc/tasklist.h"
#include <regex>
#include <sstream>
#include <iostream>
#include <numeric>


namespace Day_2024_03 {

Task::Task()
    : AocTask{"2024_03", "161", "48"} {
}

int findMultResult(const std::string& inputStr) {
    const std::regex pattern(R"(mul\((\d+),(\d+)\))");
    std::smatch matches;
    std::ostringstream result;
    std::vector<std::pair<int, int>> pairs;

    auto searchStart(inputStr.cbegin());
    while (std::regex_search(searchStart, inputStr.cend(), matches, pattern)) {
        if (matches.size() != 3) {
            throw std::runtime_error("Regex failed");
        }
        // First group is entire match, second and third groups (indexes 1 and 2) are the desired numbers
        const int num1 = std::stoi(matches[1].str());
        const int num2 = std::stoi(matches[2].str());
        pairs.emplace_back(num1, num2);
        searchStart = matches.suffix().first;
    }

    std::vector<int> multiplicated(pairs.size());
    std::transform(pairs.begin(), pairs.end(), multiplicated.begin(), [](const auto& pair) {
        const auto [num1, num2] = pair;
        return num1 * num2;
    });
    return std::accumulate(multiplicated.begin(), multiplicated.end(), 0);
}

std::string Task::partOneSolution(const std::vector<std::string>& input) {
    const std::string joinedString = std::accumulate(input.begin(), input.end(), std::string());
    return std::to_string(findMultResult(joinedString));
}

std::string Task::partTwoSolution(const std::vector<std::string>& input) {
    std::string joinedString = std::accumulate(input.begin(), input.end(), std::string());
    if (isTestMode()) {
        // In part 2, test input differs from part 1
        using namespace std::literals;
        joinedString = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"s;
    }
    const std::regex pattern(R"(don't\(\).*?do\(\))");
    joinedString = std::regex_replace(joinedString, pattern, "");

    return std::to_string(findMultResult(joinedString));
}
}
