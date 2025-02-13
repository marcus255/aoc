#include "../inc/aoc_task.h"
#include <iostream>
#include <sstream>
#include <fstream>

AocTask::AocTask(std::string name, std::string answer1, std::string answer2)
    : name{std::move(name)}, answer1{std::move(answer1)}, answer2{std::move(answer2)} {
    parseName();
    openInputFiles();
}

void AocTask::parseName() {
    size_t delimiter_pos = this->name.find('_');
    if (delimiter_pos == std::string::npos) {
        throw std::invalid_argument("Invalid format " + this->name + " for name. Expected format: YYYY_DD");
    }
    year = this->name.substr(0, delimiter_pos);
    day = this->name.substr(delimiter_pos + 1);

    if (year.empty() || day.empty()) {
        throw std::invalid_argument("Invalid format " + this->name + " for name. Expected format: YYYY_DD");
    }
}

void AocTask::openInputFiles() {
    const std::string root_path = "..";
    const std::string year_path = root_path + "/" + year;
    const std::string test_path = year_path + "/test_" + day + ".txt";
    const std::string input_path = year_path + "/input_" + day + ".txt";

    std::ifstream test_file;
    test_file.open(test_path);
    if (!test_file.is_open()) {
        throw std::runtime_error("Failed to open test file: " + test_path);
    }
    std::ifstream input_file;
    input_file.open(input_path);
    if (!input_file.is_open()) {
        throw std::runtime_error("Failed to open task file: " + input_path);
    }

    std::stringstream test_stream;
    test_stream << test_file.rdbuf();
    while (!test_stream.eof()) {
        std::string line;
        std::getline(test_stream, line);
        test_input.push_back(line);
    }

    std::stringstream input_stream;
    input_stream << input_file.rdbuf();
    while (!input_stream.eof()) {
        std::string line;
        std::getline(input_stream, line);
        task_input.push_back(line);
    }
}

void AocTask::run() {
    std::cout << "Running " << name << " Part 1 test" << std::endl;
    auto result = part1Test();
    if (result != answer1) {
        std::cerr << "Part 1 test failed. Expected: " << answer1 << " Got: " << result << std::endl;
    } else {
        std::cout << "Part 1 test passed, result: " << result << std::endl;
    }
    std::cout << "Running " << name << " Part 1" << std::endl;
    result = part1();
    std::cout << "Result: " << result << std::endl;

    std::cout << "Running " << name << " Part 2 test" << std::endl;
    result = part2Test();
    if (result != answer2) {
        std::cerr << "Part 2 test failed. Expected: " << answer2 << " Got: " << result << std::endl;
    } else {
        std::cout << "Part 2 test passed, result: " << result << std::endl;
    }
    std::cout << "Running " << name << " Part 2" << std::endl;
    result = part2();
    std::cout << "Result: " << result << std::endl;
}