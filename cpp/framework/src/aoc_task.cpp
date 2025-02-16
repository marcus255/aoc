#include "../inc/aoc_task.h"
#include <iostream>
#include <sstream>
#include <fstream>


AocTask::AocTask(std::string name, std::string answer1, std::string answer2)
    : name{std::move(name)}, answer1{std::move(answer1)}, answer2{std::move(answer2)} {
    parseName();
    loadInputFile(TaskType::Task);
    loadInputFile(TaskType::Test);
}

void AocTask::parseName() {
    size_t delimiter_pos = name.find('_');
    if (delimiter_pos == std::string::npos) {
        throw std::invalid_argument("Invalid format " + name + " for name. Expected format: YYYY_DD");
    }
    year = name.substr(0, delimiter_pos);
    day = name.substr(delimiter_pos + 1);

    if (year.empty() || day.empty()) {
        throw std::invalid_argument("Invalid format " + name + " for name. Expected format: YYYY_DD");
    }
}

void AocTask::loadInputFile(TaskType type) {
    auto& input = type == TaskType::Test ? testInput : taskInput;
    auto prefix = type == TaskType::Test ? "/test_" : "/input_";

    const std::string root_path = "..";
    const std::string year_path = root_path + "/" + year;
    const std::string input_path = year_path + prefix + day + ".txt";

    std::ifstream input_file;
    input_file.open(input_path);
    if (!input_file.is_open()) {
        throw std::runtime_error("Failed to open input file: " + input_path);
    }

    std::stringstream test_stream;
    test_stream << input_file.rdbuf();
    while (!test_stream.eof()) {
        std::string line;
        std::getline(test_stream, line);
        input.push_back(line);
    }
    input_file.close();

    if (input.empty()) {
        throw std::runtime_error("No input data loaded from file: " + input_path);
    }
}

void AocTask::runTest(const std::string &prefix, const StrVector& input, const std::string& expectedAnswer,
                      const std::function<std::string(const StrVector&)>& solutionFunc) {
    testMode = true;
    auto result = solutionFunc(input);
    auto passed = result == expectedAnswer;
    std::cout << prefix << ": " << (passed ? "\033[32m" : "\033[31m") << result;
    if (result != expectedAnswer) {
        std::cerr << " (Expected: " << expectedAnswer << ")";
    }
    std::cout << "\033[0m" << std::endl;
}

void AocTask::runTask(const std::string &prefix, const StrVector& input,
    const std::function<std::string(const StrVector&)>& solutionFunc) {
    testMode = false;
    auto result = solutionFunc(input);
    std::cout << prefix << ": " << result << std::endl;
}

void AocTask::run() {
    // TODO: add timing

    std::cout << "<<<<<<  " << year << "-" << day << "  >>>>>>" << std::endl;

    runTest("Part 1 test", testInput, answer1, [this](const StrVector& input) { return partOneSolution(input); });
    runTask("       task", taskInput, [this](const StrVector& input) { return partOneSolution(input); });

    runTest("Part 2 test", testInput, answer2, [this](const StrVector& input) { return partTwoSolution(input); });
    runTask("       task", taskInput, [this](const StrVector& input) { return partTwoSolution(input); });
    std::cout << std::endl;
}