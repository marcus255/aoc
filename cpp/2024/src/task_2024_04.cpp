#include "../inc/tasklist.h"
#include <iostream>
#include <map>
#include <memory>
#include <any>
#include <algorithm>

Task_2024_04::Task_2024_04()
    : AocTask{"2024_04", "18", "9"} {
}

using xyMap = std::map<std::pair<int, int>, char>;
using xyMapPtr = std::shared_ptr<xyMap>;

xyMapPtr getCoordinatesToChars(const std::vector<std::string>& input) {
    auto coords = std::make_shared<xyMap>();
    for (size_t y = 0; y < input.size(); y++) {
        for (size_t x = 0; x < input[y].size(); x++) {
            (*coords)[{static_cast<int>(x), static_cast<int>(y)}] = input[y][x];
        }
    }
    return coords;
}

int findNumMatches(const xyMapPtr& coords, size_t xMoves, size_t yMoves, const std::vector<std::string>& matches,
                   const std::vector<std::vector<std::pair<int, int>>>& offsets) {
    int numMatches = 0;
    for (size_t x = 0; x < xMoves; ++x) {
        for (size_t y = 0; y < yMoves; ++y) {
            for (const auto& seq_offsets : offsets) {
                std::string sequence;
                for (const auto& offset : seq_offsets) {
                    if (coords->find({x + offset.first, y + offset.second}) == coords->end()) {
                        break;
                    }
                    sequence += ((*coords)[{x + offset.first, y + offset.second}]);
                }
                if (std::find(matches.begin(), matches.end(), sequence) != matches.end()) {
                    numMatches++;
                }
            }
        }
    }
    return numMatches;
}

std::string Task_2024_04::partOneSolution([[maybe_unused]] const std::vector<std::string>& input) {
    auto coords = getCoordinatesToChars(input);

    // TODO: make saving data to taskData more elegant
    auto& data = isTestMode() ? testData : taskData;
    data = coords;

    std::vector<std::string> matches = { "XMAS", "SAMX" };
    std::vector<std::vector<std::pair<int, int>>> offsets = {
        {{0, 0}, {1, 0}, {2, 0}, {3, 0}}, // 4 letters horizontally
        {{0, 0}, {0, 1}, {0, 2}, {0, 3}}, // 4 letters vertically
        {{0, 3}, {1, 2}, {2, 1}, {3, 0}}, // 4 letters diagonally increasing
        {{0, 0}, {1, 1}, {2, 2}, {3, 3}}, // 4 letters diagonally decreasing
    };

    return std::to_string(findNumMatches(coords, input[0].size(), input.size(), matches, offsets));
}

std::string Task_2024_04::partTwoSolution([[maybe_unused]] const std::vector<std::string>& input) {
    // TODO: make loading data from taskData more elegant
    xyMapPtr coords = std::any_cast<xyMapPtr>(isTestMode() ? testData : taskData);

    std::vector<std::string> matches = { "MASMAS", "MASSAM", "SAMMAS", "SAMSAM" };
    std::vector<std::vector<std::pair<int, int>>> offsets = {
        {{0, 0}, {1, 1}, {2, 2}, {0, 2}, {1, 1}, {2, 0}}, // shape of an X, center point listed twice
    };

    return std::to_string(findNumMatches(coords, input[0].size(), input.size(), matches, offsets));
}

